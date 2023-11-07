import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

# Define functions for different pages
def render_home_page():
    st.title("Raisler Voigt, Hello")
    st.markdown("""
    I do not have any idea what I am doing here
    """)

    st.code("""
    if 2 == (1+1):
        return True
    """)
    # Add your content for the Home Page, such as dataframes, plots, etc.
# a
def render_upload_page():
    st.title("Upload Page")
    st.write("This is the Upload Page")
    # Add your content for the Upload Page, such as dataframes, plots, etc.

def render_articles_page():
    c1,c2 = st.columns(2)

    df1 = pd.DataFrame({'a': [3,2,1], 'b': ['3232', '321', '435']})
    df2 = pd.DataFrame({'a': [3,6,9], 'b': ['3232', '321', '435']})

    c1.write(df1)
    c2.write(df2)       
    st.write('ue')
    # Add your content for the Tasks Page, such as dataframes, plots, etc.

def render_settings_page():
    st.title("Settings Page")
    st.write("Configure your settings here")
    # Add your content for the Settings Page, such as dataframes, plots, etc.

# Set up the Streamlit app
st.set_page_config(page_title="Raisler Voigt", page_icon=":blue_heart:", initial_sidebar_state="collapsed")

selected2 = option_menu(None, ["Home", "Upload", "Articles", 'Settings'], 
                        icons=['house', 'cloud-upload', "list-task", 'gear'], 
                        menu_icon="cast", default_index=0, orientation="horizontal")

# Render the selected page content
if selected2 == "Home":
    render_home_page()
elif selected2 == "Upload":
    render_upload_page()
elif selected2 == "Articles":
    render_articles_page()
elif selected2 == "Settings":
    render_settings_page()

st.subheader("Buy me a coffee")
