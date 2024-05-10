# Upgrade Streamit
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

def main():
   # SETTING PAGE CONFIGURATION
   st.set_page_config(page_title='Recommendation System',layout='wide')

   # SETTING STREAMLIT STYLE
   streamlit_style = """   <style>
                           @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap');
                           
                           html,body,[class*='css']{
                              font-family:'serif';
                           }
                           </style>
                  """
   st.markdown(streamlit_style,unsafe_allow_html=True)

   # FONT STYLING FOR HEADERS
   def title(string):
         st.markdown(f"<h1 style='color:#e8322e';font-size:40px>{string}</h1>",unsafe_allow_html=True)
   def header(string):
         st.markdown(f"<h2 style='color:#FF00FF';font-size:40px>{string}</h2>",unsafe_allow_html=True)
   def subheader(string):
         st.markdown(f"<h3 style='color:#e5f55b';font-size:40px>{string}</h3>",unsafe_allow_html=True)
   def plot_subheader(string):
         st.markdown(f"<h3 style='color:#41FB3A';font-size:40px>{string}</h3>",unsafe_allow_html=True) 
   def inference_subheader(string):
         st.markdown(f"<h4 style='color:#9933ff';font-size:40px>{string}</h4>",unsafe_allow_html=True)
   def plot_subheader2(string):
         st.markdown(f"<h4 style='color:#ffff80';font-size:40px>{string}</h4>",unsafe_allow_html=True) 
         
   header('Recommendation System')
   
if __name__ == '__main__':
   main()