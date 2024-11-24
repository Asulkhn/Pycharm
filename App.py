import streamlit as st
from Pages import Home, Project1, Project2, Project3
from PIL import Image
image = Image.open('images/Th05Yin-YangOrb.png')
from streamlit_navigation_bar import st_navbar
st.set_page_config(initial_sidebar_state="collapsed")
pages = ['Home', 'Project1', 'Project2', 'Project3']
styles = {
    "nav": {
        "background-color": "red",
        "display": "flex",
        "justify-content": "center"
    },
    "img": {
      "position": "absolute",
      "left": "-20px",
      "font-size": "15px",
      "top": "4px",
      "width": "100px",
      "height": "40px",
    },
    "span": {
        "display": "block",
        "color": "white",
        "padding": "0,2rem 0.725rem",
        "font-size": "14px"
    },
    "active": {
        "background-color": "white",
        "color": "black",
        "font-weight": "normal",
        "padding": "14px"
    },
    "hover": {
        "background-color": "rgba(255, 255, 255, 0.35)",
    },
}

page = st_navbar(pages, styles=styles)

if page == 'Home':
    Home.Home().app()
elif page == "Project1":
    Project1.Project1().app()
elif page == "Project2":
    Project2.Project2().app()
elif page == "Project3":
    Project3.Project3().app()
else:
    Home.Home().app()
