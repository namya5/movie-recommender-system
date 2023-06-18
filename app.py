import streamlit as st
import pickle
import pandas as pd
import requests
st.set_page_config(layout="wide")

def fetch(movie_id):
    response = requests.get('http://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended =[]
    rec_posters=[]
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended.append(movies.iloc[i[0]].title)
        rec_posters.append(fetch(movie_id))
    return recommended,rec_posters

similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

st.markdown("""<style> 
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans&family=Figtree:wght@500&display=swap');

.big-font 
{font-size:100px !important;
 font-family: 'Figtree', sans-serif;
 text-align:left;
 color: #802BB1}
 
 .heading
 {
 padding-left:0px; margin-left:-10px;
 padding-top:100px;
 }
 
 h3
 {
 font-family: 'DM Sans', sans-serif;
  padding-left:0px; 
  padding-top: 0px;
  margin-top:-40px
 }
  div.stButton > button:first-child
 {
    background-color: #802BB1;
    padding-left:0px; margin-left:-10px;
    color: #FFFFFF;
    border:none;
    border-radius:60px;
    padding:10px;
    height:50px;
    width: 170px;
    margin-top: 50px;
 }
 #joker
 {
 height:600px;
 margin-left:600px;
 margin-top:-360px;
 padding:0px;
 margin-bottom:-200px;
 }
div[data-baseweb="select"] > div
 {
 border: 1px solid white;
 padding-top: 50px;
 margin-left=-00px;
 padding:0px;
 color: white;
 margin-top: -10px;
 width:500px;
 }
 div[data-baseweb="select"]
 {
 margin-left=-100px;
 }

</style> """, unsafe_allow_html=True)

st.markdown('<div class="heading"> <p class="big-font">CineMatch</p> </div>'
                '<h3> Your movies, your way </h3>', unsafe_allow_html=True)
option = st.selectbox('',movies['title'].values)
if st.button('Get Started'):
    names,posters = recommend(option)

    col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1])
    with col1:
            st.text(names[0])
            st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
else:
    st.markdown('<img id = "joker" src="https://i.postimg.cc/HsPJrBdM/Group-7.png" border="0" /> ',
                unsafe_allow_html=True)








