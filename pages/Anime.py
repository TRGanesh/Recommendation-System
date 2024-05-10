import streamlit as st
import pandas as pd

st.title('Anime')
anime_df = pd.read_csv('/Users/mac/Documents/ML_Projects/Movie_Recommendation_System/Datasets/anime/anime.csv')

st.dataframe(anime_df.sample(20))