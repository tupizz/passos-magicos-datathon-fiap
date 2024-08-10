import streamlit as st
import warnings
from utils.sidebar import show_sidebar

home_page = st.Page("pages/home.py", title="Home", icon=":material/home:")
create_page = st.Page("pages/analytical.py", title="Analytical", icon=":material/insights:")
model_scholarship = st.Page("pages/model_scholarship.py", title="Scholarship Prediction Model", icon="✨")
model_next_grade = st.Page("pages/model_year_pass.py", title="Student Next Grade Model", icon="✨")

pg = st.navigation([home_page, create_page, model_scholarship, model_next_grade])
st.set_page_config(layout="wide", page_title="Tech Challenge 5 | FIAP", page_icon=":material/edit:")
pg.run()

warnings.filterwarnings("ignore")

show_sidebar()