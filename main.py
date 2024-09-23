import streamlit as st
import pyjokes
import pyttsx3



# text = st.text_input('Enter some text')
if st.button('Hit me'):
  joke = pyjokes.get_joke()
  st.text(f"{joke}")
  engine = pyttsx3.init()
  engine.say(joke)
  engine.runAndWait()
