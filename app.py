import streamlit as st
import warnings
import locale

home_page = st.Page("pages/home.py", title="Home", icon=":material/home:")
create_page = st.Page("pages/analytical.py", title="Analytical", icon=":material/insights:")
delete_page = st.Page("pages/model.py", title="Model prediction", icon="✨")

pg = st.navigation([home_page, create_page, delete_page])
st.set_page_config(layout="wide", page_title="Tech Challenge 5 | FIAP", page_icon=":material/edit:")
pg.run()


warnings.filterwarnings("ignore")

try:
    locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
except locale.Error:
    locale.setlocale(locale.LC_ALL, "en_US.UTF-8")  # Fallback to a default locale

# Sidebar definitions
with st.sidebar:
    st.markdown("#")

    _, col0, _ = st.columns([1, 8, 1])

    with col0:
        st.image("assets/imgs/logo-fiap.png", width=150, use_column_width=True)

    st.divider()

    st.subheader(":blue[Aluno]")
    st.text(
        "Tadeu H. dos Reis Tupinambá Jr."
    )

    st.divider()

    st.subheader("About the project")
    st.write(
        "Este projeto foi desenvolvido para o Tech Challenge 5 da FIAP, utilizando Streamlit para a criação de uma aplicação web interativa."
    )

    st.divider()

    st.subheader("Github")
    st.link_button(
        "Main Repository",
        "https://github.com/tupizz/passos-magicos-datathon-fiap",
        help=None,
        type="secondary",
        disabled=False,
        use_container_width=False,
    )
