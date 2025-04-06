from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class VoiceSample:
    id: str
    audio_data: bytes
    transcript: str
    duration: float
    sample_rate: int
    metadata: Dict[str, Any]

import streamlit as st
import speech_recognition as sr
import language_tool_python

def analyze_audio_for_grammar(audio_file):
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Convert the uploaded file to an audio source
    with sr.AudioFile(audio_file) as source:
        st.write("Transcribing audio...")
        audio_data = recognizer.record(source)

        try:
            # Transcribe audio to text
            transcript = recognizer.recognize_google(audio_data)
            st.success("Audio transcription completed!")
            st.write("**Transcript:**", transcript)

            # Analyze transcript for grammatical mistakes
            st.write("Analyzing transcript for grammatical mistakes...")
            tool = language_tool_python.LanguageTool('en-US')
            matches = tool.check(transcript)

            if matches:
                st.warning(f"Found {len(matches)} grammatical issue(s):")
                for match in matches:
                    st.write(f"- {match.message}")
            else:
                st.success("No grammatical mistakes found!")
        except Exception as e:
            st.error(f"Error processing audio: {e}")

def upload_audio_clip():
    st.title("🎵 Audio Clip Uploader")
    st.markdown("Upload your audio clip below and analyze it for grammatical mistakes!")

    uploaded_file = st.file_uploader("Choose an audio file", type=["wav", "mp3", "ogg"])
    if uploaded_file is not None:
        st.audio(uploaded_file, format="audio/wav")
        st.success("Audio file uploaded successfully!")

        # Add a button to process the uploaded file
        if st.button("Analyze Audio"):
            with open("temp_audio.wav", "wb") as f:
                f.write(uploaded_file.read())
            analyze_audio_for_grammar("temp_audio.wav")
    else:
        st.info("Please upload an audio file to proceed.")

upload_audio_clip()