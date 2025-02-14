import streamlit as st
import pickle
import pandas as pd
import gzip


def recommend(label):
    anime_index = anime[anime['title'] == label].index[0]
    distances = similarity[anime_index]
    anime_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:7]

    recommended_anime = []
    recommended_anime_poster = []
    recommended_anime_link = []
    for i in anime_list:
        recommended_anime.append(anime.iloc[i[0]].title)
        # posters
        recommended_anime_poster.append(anime.iloc[i[0]].image)
        # links
        recommended_anime_link.append(anime.iloc[i[0]].links)
    return recommended_anime, recommended_anime_poster, recommended_anime_link


anime_dict = pickle.load(open('anime_dict.pkl', 'rb'))
anime = pd.DataFrame(anime_dict)

similarity = pickle.load(gzip.open('similarity.pkl', 'rb'))


st.title("Anime Recommender System")

select_anime_name = st.selectbox(
    "Choose Anime Name : ",
    anime['title'].values,
    index=None,
    placeholder="Select the anime for recommendation..."
)

if st.button("Recommend"):
    name, posters, link = recommend(select_anime_name)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(name[0])
        st.image(posters[0])
        st.link_button("Know More", link[0])

    with col2:
        st.write(name[1])
        st.image(posters[1])
        st.link_button("Know More", link[1])

    with col3:
        st.write(name[2])
        st.image(posters[2])
        st.link_button("Know More", link[2])

    st.write('')
    st.write('')
    st.write('')

    col4, col5, col6 = st.columns(3)

    with col4:
        st.write(name[3])
        st.image(posters[3])
        st.link_button("Know More", link[3])

    with col5:
        st.write(name[4])
        st.image(posters[4])
        st.link_button("Know More", link[4])

    with col6:
        st.write(name[5])
        st.image(posters[5])
        st.link_button("Know More", link[5])
