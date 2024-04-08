import streamlit as st
import pandas as pd

# Audio
audio_file = open('D:\Steamlit\\audio.ogg', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/ogg')

# video 

video_file = open('D:\Songs\\Arabic kutty.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)