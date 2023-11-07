import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu


from st_pages import Page, show_pages, add_page_title

st.set_page_config(page_title="Raisler Voigt", page_icon=":blue_heart:", initial_sidebar_state="collapsed")


selected2 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
icons=['house', 'cloud-upload', "list-task", 'gear'], 
menu_icon="cast", default_index=0, orientation="horizontal")

st.title("Hello Fellas")
st.markdown("""
I do not have any idea what I am doing here
""")

st.code("""
if 2 == (1+1):
    return True
""")


# START HERE


c1,c2,c3 = st.columns(3)

with c1:
    st.button('articles', on_click=render_page('articles'))

st.subheader("Buy me a coffee")


