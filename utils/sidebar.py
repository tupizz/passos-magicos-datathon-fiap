import streamlit as st


def show_sidebar():
    # Sidebar definitions
    with st.sidebar:
        st.markdown("#")

        _, col0, _ = st.columns([1, 8, 1])

        with col0:
            st.image("assets/imgs/logo-fiap.png", width=150, use_column_width=True)

        st.divider()

        st.subheader("About the project")
        st.write(
            "Este projeto foi desenvolvido para o Tech Challenge 5 da FIAP, utilizando Streamlit para a criação de uma aplicação web interativa."
        )

        st.divider()

        st.subheader(":blue[Aluno]")
        st.text(
            "Tadeu H. dos Reis Tupinambá Jr."
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
