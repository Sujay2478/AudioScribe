import streamlit as st
import whisper
from fpdf import FPDF
from docx import Document
import io

st.title("AudioScribe")

# Upload audio file with Streamlit
audio_file = st.file_uploader("Upload Audio", type=["wav", "mp3", "m4a"])

model = whisper.load_model("base")
st.text("Audio Loaded")

# Helper function to format seconds into HH:MM:SS
def format_time(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return "{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds))

# Function to save transcript as TXT
def save_transcript_txt(transcript):
    buffer = io.StringIO()
    buffer.write(transcript)
    buffer.seek(0)
    return buffer.getvalue().encode('utf-8')  # Convert to bytes

# Function to save transcript as PDF
def save_transcript_pdf(transcript):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in transcript.split('\n'):
        pdf.cell(200, 10, txt=line, ln=True, align='L')
    pdf_output = io.BytesIO()
    pdf.output(dest='S', name=pdf_output)  # Save to BytesIO buffer
    pdf_output.seek(0)
    return pdf_output

# Function to save transcript as DOCX
def save_transcript_docx(transcript):
    doc = Document()
    for line in transcript.split('\n'):
        doc.add_paragraph(line)
    docx_output = io.BytesIO()
    doc.save(docx_output)
    docx_output.seek(0)
    return docx_output

# Transcribe Audio
if st.sidebar.button("Transcribe Audio"):
    if audio_file is not None:
        st.sidebar.success("Transcribing Audio")
        result = model.transcribe(audio_file.name)
        full_transcript = ""
        
        # Compiling the full transcript
        for segment in result['segments']:
            start_time = format_time(segment['start'])
            end_time = format_time(segment['end'])
            transcript = segment['text']
            full_transcript += f"{start_time} - {end_time}: {transcript}\n"
            st.write(f"{start_time} - {end_time}: {transcript}")
        
        st.sidebar.success("Transcription Complete")

        # Export options
        st.sidebar.header("Export Transcription")
        txt_data = save_transcript_txt(full_transcript)
        st.sidebar.download_button(label="Download TXT", data=txt_data, file_name="transcript.txt", mime='text/plain')
        
        pdf_buffer = save_transcript_pdf(full_transcript)
        st.sidebar.download_button(label="Download PDF", data=pdf_buffer, file_name="transcript.pdf", mime='application/pdf')

        docx_buffer = save_transcript_docx(full_transcript)
        st.sidebar.download_button(label="Download DOCX", data=docx_buffer, file_name="transcript.docx", mime='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    else:
        st.sidebar.error("Please upload an audio file")

# Play Original Audio File
st.sidebar.header("Play Original Audio File")
st.sidebar.audio(audio_file)







