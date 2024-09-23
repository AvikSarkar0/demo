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
import io

if st.button('Hit me'):
    joke = pyjokes.get_joke()
    st.text(f"{joke}")

    # Convert joke to speech using gTTS
    tts = gTTS(joke)
    
    # Save to an in-memory file object
    audio_file = io.BytesIO()
    tts.write_to_fp(audio_file)
    audio_file.seek(0)  # Move to the start of the file

    # Play the audio in Streamlit using st.audio
    st.audio(audio_file, format='audio/mp3')
