import streamlit as st


def show_sidebar():
    # Sidebar definitions
    with st.sidebar:

        # Student section
        st.subheader(":green[Aluno]")
        st.text(
            "Tadeu H. dos Reis Tupinambá Jr."
        )
        st.text("Matrícula: RM351125")

        # About
        st.divider()
        st.subheader(":green[About the project]")
        st.write(
            "Este projeto foi desenvolvido para o Tech Challenge 5 da FIAP, utilizando Streamlit para a criação de uma aplicação web interativa."
        )

        # Repository
        st.divider()
        st.subheader(":green[Github]")
        st.link_button(
            "Main Repository",
            "https://github.com/tupizz/passos-magicos-datathon-fiap",
            help="Link to the main repository on GitHub.",
            type="secondary",
            disabled=False,
            use_container_width=True,
        )

        # Fiap Logo
        st.divider()
        _, col0, _ = st.columns([1, 3, 1])

        with col0:
            st.image("assets/imgs/logo-fiap.png", width=150)

