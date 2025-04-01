from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import speech_recognition as sr
from transformers import pipeline
from io import BytesIO
from pydub import AudioSegment

app = FastAPI()

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development; change for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize NLP models for summarization and sentiment analysis
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", tokenizer="facebook/bart-large-cnn")
sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Convert audio file to text using SpeechRecognition
def audio_to_text(audio_bytes):
    recognizer = sr.Recognizer()
    try:
        # Convert audio to WAV format (in case of MP3, M4A, etc.)
        audio = AudioSegment.from_file(BytesIO(audio_bytes))
        audio = audio.set_channels(1).set_frame_rate(16000)  # Convert to mono, 16kHz
        audio_wav = BytesIO()
        audio.export(audio_wav, format="wav")
        audio_wav.seek(0)
        
        # Recognize speech in the audio
        with sr.AudioFile(audio_wav) as source:
            audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
        return text
    except Exception as e:
        return f"Error: {str(e)}"

# Summarize the transcribed text using Hugging Face's summarizer
def summarize_text(text):
    try:
        # Truncate text if it exceeds the maximum input length for the model
        max_input_length = 1024
        if len(text) > max_input_length:
            text = text[:max_input_length]  # Truncate if too long
        summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        return f"Summarization Error: {str(e)}"

# Analyze sentiment of the transcribed text
def analyze_sentiment(text):
    try:
        sentiment = sentiment_analyzer(text)
        return sentiment[0]['label']
    except Exception as e:
        return f"Sentiment Analysis Error: {str(e)}"

# FastAPI route for processing the audio file
@app.post("/process_audio/")
async def process_audio(file: UploadFile = File(...)):
    try:
        audio_bytes = await file.read()

        # Get the transcript from the audio file
        transcript = audio_to_text(audio_bytes)

        if transcript.startswith("Error:"):
            return {"error": transcript}

        # Summarize the transcript
        summary = summarize_text(transcript)

        # Analyze sentiment of the transcript
        sentiment = analyze_sentiment(transcript)

        # Return the response with transcript, summary, and sentiment
        return {
            "transcript": transcript,
            "summary": summary,
            "sentiment": sentiment
        }

    except Exception as e:
        return {"error": f"Processing failed: {str(e)}"}
