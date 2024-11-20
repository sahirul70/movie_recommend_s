import streamlit as st
import pickle
import pandas as pd
import requests



movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movie_df = pd.DataFrame(movies_dict)
similarities = pickle.load(open('similarities.pkl','rb')) 

def fatch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommand(movie):
    movies_index = movie_df[movie_df['title']==movie].index[0]
    similarity = similarities[movies_index]
    movies_list = sorted(list(enumerate(similarity)), reverse = True, key = lambda x:x[1])[1:6]
    
    recommanded_moveis=[]
    recommanded_moveis_posters=[]
    for i in movies_list:
        movie_id = movie_df.iloc[i[0]].movie_id
        recommanded_moveis.append(movie_df.iloc[i[0]].title)
        recommanded_moveis_posters.append(fatch_poster(movie_id))
    return recommanded_moveis,recommanded_moveis_posters

st.title("Movie Reconmmendation System")

selected_movie_name = options =st.selectbox("How would like to be a contacted",movie_df["title"].values)
if st.button("Reconmmend"):
    names,posters = recommand(selected_movie_name)
    # for i in recommandtions:
    #     st.write(i)
    #recommended_movie_names,recommended_movie_posters =recommand(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
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
