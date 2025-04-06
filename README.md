# Audio Grammar Analyzer 🎵📝

## Overview

**Audio Grammar Analyzer** is a Streamlit-based web application that allows users to upload audio files, transcribe them into text, and analyze the transcription for grammatical mistakes. It combines audio-to-text transcription with grammar-checking functionality to provide a seamless experience.

## Features

- Upload audio files in `.wav`, `.mp3`, or `.ogg` formats.
- Transcribe audio to text using the Google Speech Recognition API.
- Analyze the transcribed text for grammatical mistakes using `language_tool_python`.
- Display the transcription and highlight grammatical issues.

## Installation

### Prerequisites

- Python 3.7 or higher
- Pip (Python package manager)

### Steps

1. Clone the repository or download the project files:

   ```bash
   git clone <repository-url>
   cd SHL
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have the following libraries installed:

   - `streamlit`
   - `speechrecognition`
   - `language-tool-python`

   If not, install them manually:

   ```bash
   pip install streamlit speechrecognition language-tool-python
   ```

## Usage

1. Run the Streamlit app:

   ```bash
   streamlit run models/voice_sample.py
   ```

2. Open the app in your browser (usually at `http://localhost:8501`).

3. Upload an audio file and click "Analyze Audio" to view the transcription and grammatical analysis.

## Project Structure

```
SHL/
├── models/
│   └── voice_sample.py  # Main application logic
├── README.md            # Project documentation
└── requirements.txt     # List of dependencies
```

## Example

1. Upload an audio file:
   - Supported formats: `.wav`, `.mp3`, `.ogg`
2. View the transcription:
   ```
   Transcript: "This is an example sentence."
   ```
3. Analyze grammatical mistakes:
   ```
   Found 1 grammatical issue(s):
   - Possible typo: Did you mean "an example"?
   ```

## Dependencies

- [Streamlit](https://streamlit.io/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [LanguageTool](https://pypi.org/project/language-tool-python/)

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- [Google Speech Recognition API](https://cloud.google.com/speech-to-text)
- [LanguageTool](https://languagetool.org/)
