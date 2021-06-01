#Do the imports

import streamlit as st
import pages.home
import pages.data_analyze
import base64
from PIL import Image
import resources.ast as ast

#Navigation bar
PAGES = {
    "Home": pages.home,
    "Data Analysis": pages.data_analyze
    
}

def main():
    st.sidebar.title("Navigation bar")
    selection = st.sidebar.radio("Go To", list(PAGES.keys()))

    page = PAGES[selection]
    
    with st.spinner(f"Loading {selection} ..."):
        ast.write_page(page)

    st.sidebar.title("About Us")
    st.sidebar.info(
        """
        We are AI team from Strive School.
        """
    )



unsafe_allow_html = True

if __name__ == "__main__":
    main()

