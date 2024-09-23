import pyttsx3
import streamlit as st

engine = pyttsx3.init()
text = st.text_input('Enter some text')
engine.say(text=text)
engine.runAndWait()


"""
streamlit run main.py
"""