import streamlit as st
import pandas as pd

st.title('Movies')
movies_df = pd.read_csv('/Users/mac/Documents/ML_Projects/Movie_Recommendation_System/Datasets/TMDB_movie_dataset_v11_1M_Dataset.csv')

st.dataframe(movies_df.sample(20),use_container_width=True)