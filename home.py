import streamlit as st
import base64
from PIL import Image
import webbrowser

def write():
    st.title("Home")
    st.write("![Your Awsome GIF](https://assets.vogue.com/photos/5f5fac8b7d9362f52d645560/16:9/w_1280,c_limit/social-holding.jpg)")
    st.markdown(
    """## About the project

    Zalando is an European e-commerce company based in Berlin, offering fashion and lifestyle products to customers in 17 European markets.
    """
    )

    container = st.beta_container()
    container.markdown(
    """## Missons

    Zalando popularized the “free return policy”. However
    “About half of the products Zalando sells are returned”
    / Everytime a product is returned, an employee has to understand which product it is, read the label, the size and so on.
    / Once she/he figured out which one is the right one, the employee has to search for the right section to put the product on the shelf.
    / A lot of precious resources are wasted!


    """
    )





#Give the details of the team
def dummy_fun():
    st.markdown("## Members:")
    if st.button('Hadaya Ali'):
        webbrowser.open_new_tab('https://www.linkedin.com/in/hedaya-ali/')
    elif st.button('Stephen George'):
        webbrowser.open_new_tab('https://www.linkedin.com/in/stephen-george-b79941116/')
    elif st.button('Thanh Nguyen'):
        webbrowser.open_new_tab('https://www.linkedin.com/in/nguyenphuocxuanthanh/')
    elif st.button('Gabriel Pasca '):
        webbrowser.open_new_tab('https://www.linkedin.com/in/gabrielmpasca/')

write()
dummy_fun()