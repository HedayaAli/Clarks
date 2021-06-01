import streamlit as st
import plotly.express as px
import pandas as pd
import time
import numpy as np

def write():
    st.title("Data Analysis :door:")
    st.write("\n")
    st.write("\n")
    st.markdown(
           """### Let's explore the dataframe with us
            / Fashione-MNIST is a dataset of Zalando’s article images
            / training set: 60k 28x28 grayscale images
            / test set: 10k 28x28 grayscale images
            / 10 clothing classes
           """
    )




    st.header("**DataFrame**:")

    #Prompt the user to upload a csv file
    uploaded_file = st.file_uploader("Please choose a .CSV file", type=['csv'])
    if uploaded_file is not None:
        # do stuff
        df = pd.read_csv(uploaded_file)
        df1 = df.head()

  

    st.markdown(""" You can select one of the following two options where you can choose between displaying
    the complete DataFrame or just the head (first five rows of the DataFrame).""")

    #Widgets for showing the DataFrame
    if st.button("Click here to see the full df"):
        with st.spinner('Loading the full DataFrame...'):
            time.sleep(4)
            #round_float()
    elif st.button("Click here to see the head"):
        with st.spinner('Loading the head of the DataFrame...'):
            time.sleep(3)
       # round_float_head()

    st.write("\n")
    st.write("\n")
    st.markdown("Now that you know how the data looks like. It's time for some analysis...")




    #User interactive analysis
    st.write("\n")
    st.write("\n")
    st.header("**A playground for Data Analysis** :football:")
    st.markdown("""Inorder to analyse the data we've implemented an interface where _you_ as a user 
    can interact with the dataset and play with it.\n""")

    #A tab where an user can select the columns that he wants to display
    interactive_col = st.multiselect("Please select the columns that you want to display from the above data.", df.columns)


    #Make the plots
    st.header("**Insights** :chart:")
    st.markdown("### Piano piano ... step by step we analyze the data together:")



    #Feature Engineering 
    st.markdown("Model Description")
    st.image("model_summary.PNG")
    st.image("model structure.PNG")


