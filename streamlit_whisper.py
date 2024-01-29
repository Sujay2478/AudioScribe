# conda install ffmpeg

# Installing pytorch
# conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia

# Installing Whisper
# pip install git+https://github.com/openai/whisper.git -q

# pip install streamlit
import streamlit as st
import whisper

st.title("AudioScribe")

# upload audio file with streamlit
audio_file = st.file_uploader("Upload Audio", type=["wav", "mp3", "m4a"])

model = whisper.load_model("base")
st.text("Audio Loaded")


def format_time(seconds):
    """ Helper function to format seconds into HH:MM:SS """
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return "{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds))


if st.sidebar.button("Transcribe Audio"):
    if audio_file is not None:
        st.sidebar.success("Transcribing Audio")
        result = model.transcribe(audio_file.name)
        st.sidebar.success("Transcription Complete")
        
        # Displaying segments with timestamps
        for segment in result['segments']:
            start_time = format_time(segment['start'])
            end_time = format_time(segment['end'])
            transcript = segment['text']
            st.write(f"{start_time} - {end_time}: {transcript}")
    else:
        st.sidebar.error("Please upload an audio file")


st.sidebar.header("Play Original Audio File")
st.sidebar.audio(audio_file)







