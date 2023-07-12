import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

col1, col2, col3 = st.columns(3)
col2.image(Image.open('bobo.png'))

st.header('David Cheung, Developer')

st.info('Have fun with ChatGPT')

icon_size = 20
# Import and Query



st_button('medium', 'https://import-2-vector.streamlit.app', 'vectorization to embedding', icon_size)
st_button('medium', 'https://hug-bot.streamlit.app/', 'Hug Chat', icon_size)
st_button('medium', 'https://recommend-cs.streamlit.app/', 'recommend products', icon_size)
st_button('medium', 'https://prompt-runner.streamlit.app/', 'Prompt Runner', icon_size)
st_button('medium', 'https://pdf-automation.streamlit.app/', 'Ask Resume PDF file II', icon_size)
st_button('medium', 'https://askpdf-by-david.streamlit.app/', 'Ask Resume PDF file I', icon_size)
st_button('medium', 'https://csv-sqldb.streamlit.app/', 'Ask any CSV file', icon_size)
st_button('medium', 'https://smart-csv.streamlit.app/', 'Ask  CSV by ai', icon_size)

st_button('medium', 'https://ask-studyplan.streamlit.app/', 'Summarize your Study Plan', icon_size)
st_button('medium', 'https://ask-orders-csv.streamlit.app/', 'Summarize your Customers Orders', icon_size)
st_button('medium', 'https://xls-loader.streamlit.app/', 'Visualize your Excel Sheet', icon_size)






# Generative Creation 
st_button('medium', 'https://storymaker-by-david.streamlit.app/', 'Create your Story', icon_size)
st_button('medium', 'https://questions-maker-by-david.streamlit.app/', 'Create your Article & Questions-Answer', icon_size)
st_button('medium', 'https://story-ppt-david.streamlit.app/', 'See Comic Book created by MidJourney ', icon_size)
# Search & Analsis
st_button('medium', 'https://search-by-david.streamlit.app/', 'Google Now', icon_size)
st_button('medium', 'https://stockwatch-by-david.streamlit.app/', 'Stock Watch', icon_size)
