import streamlit as st
import warnings

import locale

warnings.filterwarnings("ignore")
warnings.filterwarnings("ignore")
locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
st.set_page_config(
    page_title="Tech Challenge 5 | FIAP", layout="wide"
)

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

st.title('Hello, Streamlit!')
st.write('Welcome to your first Streamlit app.')