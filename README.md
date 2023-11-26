# AudioScribe

## Introduction
AudioScribe is a web application built with Streamlit that utilizes OpenAI's Whisper model for transcribing audio files. It offers a user-friendly interface for uploading audio files in various formats (WAV, MP3, M4A) and receiving their transcriptions.

## Requirements
- Python
- Conda package manager
- NVIDIA GPU for CUDA (optional but recommended for performance)

## Installation

### Setting up the Environment
1. Install Conda from the [official Conda website](https://www.anaconda.com/products/distribution) if not already installed.
2. It's recommended to create a new Conda environment for this project.

### Install Dependencies
Execute the following commands in your Conda environment:

# Install FFmpeg
conda install ffmpeg

# Install PyTorch with CUDA Support
conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia

# Install Whisper
pip install git+https://github.com/openai/whisper.git -q

# Install Streamlit
pip install streamlit

##Running the application
streamlit run streamlit_whisper.py


