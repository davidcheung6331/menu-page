import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

col1, col2, col3 = st.columns(3)
col2.image(Image.open('bobo.png'))

st.header('David Cheung, Developer')

st.info('Have fun with ChatGPT')

icon_size = 20

st_button('medium', 'https://stockwatch-by-david.streamlit.app/', 'Stock Watch', icon_size)
st_button('medium', 'https://askpdf-by-david.streamlit.app/', 'Ask your PDF file', icon_size)
st_button('medium', 'https://search-by-david.streamlit.app/', 'Google Now', icon_size)
st_button('medium', 'https://storymaker-by-david.streamlit.app/', 'Story Maker', icon_size)
st_button('medium', 'https://questions-maker-by-david.streamlit.app/', 'Article and Multiple Choice Maker', icon_size)
st_button('medium', 'https://story-ppt-david.streamlit.app/', 'Comic Book Presentation by MidJourney ', icon_size)
