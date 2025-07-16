import pyaudio
import wave
import os
import time
import json
import boto3
from botocore.exceptions import ClientError
import assemblyai as aai
from gpiozero import Button, LED
from signal import pause
import threading
from multiprocessing import Event
import atexit

# ---------------------- CONFIGURATION ----------------------

# Audio recording parameters
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

# AssemblyAI API key
aai.settings.api_key = "4342dd3e0a584dc1a279b412ac509b98"

# AWS S3 bucket details
BUCKET_NAME = 'rosetta2'
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID", "PUT-YOUR-KEY-HERE")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY", "PUT-YOUR-SECRET-HERE")

# GPIO Pins
BUTTON_START_PIN = 12
BUTTON_STOP_PIN = 26
LED_PIN = 16

# ---------------------- GLOBAL VARIABLES ----------------------

is_recording = False
stop_event = Event()
process = None
audio_file_path = ""
transcription_file_path = ""

# ---------------------- FUNCTION DEFINITIONS ----------------------

def record_audio(file_path, stop_event):
    """Record audio until stop_event is set."""
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    
    frames = []
    print(f"Recording to {file_path}")

    try:
        while not stop_event.is_set():
            data = stream.read(CHUNK, exception_on_overflow=False)
            frames.append(data)
    except Exception as e:
        print(f"Recording error: {e}")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open(file_path, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

    print(f"Audio saved: {file_path}")

def transcribe_audio(file_path):
    """Transcribe audio using AssemblyAI."""
    transcriber = aai.Transcriber()
    print(f"Transcribing {file_path}...")
    
    transcript = transcriber.transcribe(file_path)
    
    if transcript.status == aai.TranscriptStatus.completed:
        print("Transcription completed.")
        return transcript.text
    else:
        print(f"Transcription failed: {transcript.error}")
        return None

def upload_to_s3(bucket_name, source_file, destination_path):
    """Upload file to AWS S3."""
    s3_client = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )

    try:
        s3_client.upload_file(source_file, bucket_name, destination_path)
        print(f"Uploaded {source_file} to s3://{bucket_name}/{destination_path}")
    except ClientError as e:
        print(f"S3 upload error: {e}")

def process_and_upload(audio_path, transcript_path):
    """Transcribe, save, and upload audio and transcript."""
    transcription = transcribe_audio(audio_path)

    if transcription:
        os.makedirs(os.path.dirname(transcript_path), exist_ok=True)
        with open(transcript_path, 'w') as f:
            json.dump({"transcription": transcription}, f, indent=4)
        print(f"Transcription saved: {transcript_path}")

        upload_to_s3(BUCKET_NAME, audio_path, f'audio/{os.path.basename(audio_path)}')
        upload_to_s3(BUCKET_NAME, transcript_path, f'transcriptions/{os.path.basename(transcript_path)}')
    else:
        print("No transcription generated.")

    for file in [audio_path, transcript_path]:
        if os.path.exists(file):
            os.remove(file)
            print(f"Deleted local file: {file}")

def start_recording():
    global is_recording, process, stop_event, audio_file_path, transcription_file_path

    if is_recording:
        print("Already recording.")
        return

    is_recording = True
    led.on()
    print("Recording started. Press stop button to end.")

    timestamp = time.strftime("%Y%m%d_%H%M%S")
    audio_file_path = f"recorded_audio_{timestamp}.wav"
    transcription_file_path = f"transcriptions/transcription_{timestamp}.json"

    stop_event.clear()
    process = threading.Thread(target=record_audio, args=(audio_file_path, stop_event))
    process.start()

def stop_recording():
    global is_recording, process, stop_event

    if not is_recording:
        print("Not currently recording.")
        return

    is_recording = False
    led.off()
    stop_event.set()

    if process:
        process.join()

    print("Recording stopped. Processing file...")
    process_and_upload(audio_file_path, transcription_file_path)

def cleanup():
    print("Cleaning up resources...")

# ---------------------- MAIN EXECUTION ----------------------

if __name__ == "__main__":
    button_start = Button(BUTTON_START_PIN)
    button_stop = Button(BUTTON_STOP_PIN)
    led = LED(LED_PIN)

    os.makedirs("transcriptions", exist_ok=True)
    atexit.register(cleanup)

    button_start.when_pressed = start_recording
    button_stop.when_pressed = stop_recording

    print("System ready. Press start button to record.")
    pause()


# ---------------------- MAIN EXECUTION ----------------------
