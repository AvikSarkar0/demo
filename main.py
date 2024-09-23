# import streamlit as st
# import pyjokes
# import pyttsx3



# # text = st.text_input('Enter some text')
# if st.button('Hit me'):
#   joke = pyjokes.get_joke()
#   st.text(f"{joke}")
#   engine = pyttsx3.init()
#   engine.say(joke)
#   engine.runAndWait()


import streamlit as st
import pyjokes
from gtts import gTTS
import os

if st.button('Hit me'):
    joke = pyjokes.get_joke()
    st.text(f"{joke}")

    # Convert joke to speech using gTTS
    tts = gTTS(joke)
    tts.save('joke.mp3')
    os.system('mpg123 joke.mp3')  # Play the saved MP3 file
