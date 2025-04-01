from pydub import AudioSegment
import speech_recognition as sr

def transcribe_audio(file_path):
    # Convert M4A to WAV using pydub if the file is in M4A format
    if file_path.endswith(".m4a"):
        audio = AudioSegment.from_file(file_path, format="m4a")
        wav_path = file_path.replace(".m4a", ".wav")
        audio.export(wav_path, format="wav")
        file_path = wav_path  # Update file path to the new WAV file

    recognizer = sr.Recognizer()
    
    # Read the audio file
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)

    try:
        # Try transcribing the audio using Google Speech Recognition API
        transcript = recognizer.recognize_google(audio)
        print(f"Transcript: {transcript}")  # Log the transcript to console for debugging
        return transcript
    except sr.UnknownValueError:
        print("Could not understand the audio.")  # Handle unintelligible audio
        return "Could not understand audio."
    except sr.RequestError as e:
        print(f"API unavailable. Error: {str(e)}")  # Handle API request errors
        return f"API unavailable. Error: {str(e)}"
