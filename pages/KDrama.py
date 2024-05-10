import streamlit as st
import pandas as pd

st.title('KDrama')

kDrama_df = pd.read_csv('/Users/mac/Documents/ML_Projects/Movie_Recommendation_System/Datasets/k_Drama/all_series.csv')

st.dataframe(kDrama_df.sample(20))