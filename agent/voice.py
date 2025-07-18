import pyttsx3
import whisper

model = whisper.load_model("base")

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def speech_to_text(audio_path):
    result = model.transcribe(audio_path)
    return result["text"]
