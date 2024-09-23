import streamlit as st
import pyjokes


# text = st.text_input('Enter some text')
if st.button('Hit me'):
  joke = pyjokes.get_joke()
  st.text(f"{joke}")


