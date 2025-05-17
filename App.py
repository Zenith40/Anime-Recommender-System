import streamlit as st
import pickle
import pandas as pd



def recommend(label):
    anime_index = anime[anime['title'] == label].index[0]
    distances = similarity[anime_index]
    anime_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:10]

    recommended_anime = []
    recommended_anime_poster = []
    recommended_anime_link = []
    for i in anime_list:
        recommended_anime.append(anime.loc[i[0]].title)
        # posters
        recommended_anime_poster.append(anime.loc[i[0]].image)
        # links
        recommended_anime_link.append(anime.loc[i[0]].links)
    return recommended_anime, recommended_anime_poster, recommended_anime_link


anime_dict = pickle.load(open('anime_dict.pkl', 'rb'))
anime = pd.DataFrame(anime_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))


st.title("Anime Recommender System")

select_anime_name = st.selectbox(
    "Choose Anime Name : ",
    anime['title'].values,
    index=None,
    placeholder="Select the anime for recommendation..."
)


if st.button("Recommend",use_container_width=True):

    st.write('')
    st.write('')
    st.write('')

    name, posters, link = recommend(select_anime_name)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(posters[0])
        st.write(name[0])
        st.write('')
        st.link_button("Know More", link[0],use_container_width=True)

    with col2:
        st.image(posters[1])
        st.write(name[1])
        st.write('')
        st.link_button("Know More", link[1],use_container_width=True)

    with col3:
        st.image(posters[2])
        st.write(name[2])
        st.write('')
        st.link_button("Know More", link[2],use_container_width=True)

    st.write('')
    st.write('')
    st.write('')

    col4, col5, col6 = st.columns(3)

    with col4:
        st.image(posters[3])
        st.write(name[3])
        st.write('')
        st.link_button("Know More", link[3],use_container_width=True)

    with col5:
        st.image(posters[4])
        st.write(name[4])
        st.write('')
        st.link_button("Know More", link[4],use_container_width=True)

    with col6:
        st.image(posters[5])
        st.write(name[5])
        st.write('')
        st.link_button("Know More", link[5],use_container_width=True)

    st.write('')
    st.write('')
    st.write('')

    col7, col8, col9 = st.columns(3)

    with col7:
        st.image(posters[6])
        st.write(name[6])
        st.write('')
        st.link_button("Know More", link[6],use_container_width=True)

    with col8:
        st.image(posters[7])
        st.write(name[7])
        st.write('')
        st.link_button("Know More", link[7],use_container_width=True)

    with col9:
        st.image(posters[8])
        st.write(name[8])
        st.write('')
        st.link_button("Know More", link[8],use_container_width=True)
