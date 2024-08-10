import streamlit as st
import warnings
from utils.sidebar import show_sidebar

home_page = st.Page("pages/home.py", title="Home", icon=":material/home:")
create_page = st.Page("pages/analytical.py", title="Analytical", icon=":material/insights:")
delete_page = st.Page("pages/model.py", title="Model prediction", icon="✨")

pg = st.navigation([home_page, create_page, delete_page])
st.set_page_config(layout="wide", page_title="Tech Challenge 5 | FIAP", page_icon=":material/edit:")
pg.run()

warnings.filterwarnings("ignore")

show_sidebar()