import pickle
import pandas as pd
import streamlit as st
import json
from urllib.request import urlopen

hide_menu = """
<style>
#MainMenu {
    visibility:hidden;
}
</style>
"""
text_color = """
<style>
"""

# Api Queries
api = "https://www.googleapis.com/books/v1/volumes?q="
key = "" # Optionally insert Your api Key as "&key=<your api key>"

default_img = "default_cover.png"

# loading DB's
book_dict = pickle.load(open('finbook_dict.pkl', 'rb'))
recommendations = pickle.load(open('fin_recommend.pkl', 'rb'))
books = pd.DataFrame(book_dict)

# Fetch Image Link
def fetchimg(title):
    title = title.replace(" ", "%20")
    title = title.replace("'", "%27")
    url = api + title + key
    # send a request and get a JSON response
    resp = urlopen(url)
    # parse JSON into Python as a dictionary
    books_data = json.load(resp)
    if books_data["totalItems"] == 0:
        return default_img
    book_data = books_data["items"][0]
    try:
        image_links = book_data["volumeInfo"]["imageLinks"]
    except:
        return default_img
    return image_links["thumbnail"]


# Recommendation Function
def recommend(list):
    volumes = []
    for i in list:
        volume = {}
        volume['title'] = books.iloc[i].title
        volume['author'] = books.iloc[i].author
        volume['img_link'] = fetchimg(volume['title']) 
        volumes.append(volume)
    return volumes


# Page Content
st.set_page_config(page_title="Book Recommender", page_icon=":books:", layout="wide")
st.title("Book Recommendation System")
st.markdown(hide_menu, unsafe_allow_html=True)

# Input
book_option = st.selectbox("Book Title :", books['title'].values)
if st.button("Recommend"):
    # Recommendations
    volumes = recommend(recommendations[(books[books['title'] == book_option].index[0])])
    with st.container():
        Book1, Book2, Book3, Book4, Book5 = st.columns(5)

        with Book1:
            st.image(image=volumes[0]['img_link'])
            st.write(volumes[0]['title'])
            st.write("By " + volumes[0]['author'])
        with Book2:
            st.image(image=volumes[1]['img_link'])
            st.write(volumes[1]['title'])
            st.write("By " + volumes[1]['author'])
        with Book3:
            st.image(image=volumes[2]['img_link'])
            st.write(volumes[2]['title'])
            st.write("By " + volumes[2]['author'])
        with Book4:
            st.image(image=volumes[3]['img_link'])
            st.write(volumes[3]['title'])
            st.write("By " + volumes[3]['author'])
        with Book5:
            st.image(image=volumes[4]['img_link'])
            st.write(volumes[4]['title'])
            st.write("By " + volumes[4]['author'])

with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("Made by Hari Acharya")
    with col2:
        st.write("[Github](https://github.com/Eklvya13/Book-Recommender)")

