#tools.py
from crewai import LLM
import os
os.environ["PATH"] = "C:\\ffmpeg\\bin;" + os.environ["PATH"]
import whisper
import warnings
warnings.filterwarnings("ignore")


# Load Whisper model once
whisper_model = whisper.load_model("base")

def return_audio_text(audio_path):
    result = whisper_model.transcribe(audio_path)
    return print("The transcribed Audio is: " + result["text"])

# ---------- AUDIO TOOL ----------
def speech_to_text(audio_path: str) -> str:
    try:
        result = whisper_model.transcribe(audio_path)
        return result["text"]
    except Exception as e:
        return f"ERROR: audio processing failed - {str(e)}"


# ---------- IMAGE TOOL ----------
def moondream_vision(image_path: str) -> str:
    try:
        llm = Ollama(model="moondream")
        prompt = f"Describe ONLY factual visible elements in this image: {image_path}"
        return llm.invoke(prompt)
    except Exception as e:
        return f"ERROR: image processing failed - {str(e)}"


# ---------- VALIDATION TOOL ----------
def validate_modalities(audio_text: str, image_text: str) -> str:
    """
    Strict validation logic (no LLM here → avoids hallucination)
    """
    report = []

    if not audio_text.strip():
        report.append("Audio missing or unclear")

    if not image_text.strip():
        report.append("Image description missing")

    # Simple contradiction detection (expand later)
    if "red" in audio_text.lower() and "blue" in image_text.lower():
        report.append("Conflict: audio says red, image shows blue")

    if not report:
        report.append("No obvious conflicts detected")

    return "\n".join(report)