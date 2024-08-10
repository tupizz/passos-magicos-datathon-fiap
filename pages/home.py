# page2.py
import streamlit as st

with st.container():
    col0, col1 = st.columns([7, 3])

    with col0:
        st.header(f":orange[Passos Mágicos - Datathon FIAP {2024}]")

    st.markdown(
        """
            The Passos Mágicos Association has a 31-year history of working to transform the lives of low-income children and young people, helping them access better life opportunities.

            The transformation, envisioned by Michelle Flues and Dimetri Ivanoff, began in 1992, working within orphanages in the municipality of Embu-Guaçu.

            In 2016, after years of activity, they decided to expand the program so that more young people could have access to this magical formula for transformation, which includes: quality education, psychological/psychopedagogical support, broadening their worldview, and fostering leadership. They then began operating as a social and educational project, thus creating the Passos Mágicos Association.
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        ### Main Objective
        
        The main objective of the Datathon is for you, as a data scientist, to create a predictive proposal or, as a data analyst, to develop an analytical proposal to demonstrate the impact that the NGO "Passos Mágicos" has been making on the community it serves. The association seeks to empower the use of education as a tool for changing the living conditions of children and young people in social vulnerability. Based on the extensive research dataset on educational development from the period of 2020, 2021, and 2023, you can deliver one of the following proposals:
    
        Analytical Proposal: Create a storytelling to demonstrate the impacts that the NGO "Passos Mágicos" has had on student performance and raise performance indicators. The idea is to create a dashboard and storytelling by telling a story with the data to help Passos Mágicos make the best decisions based on the indicators and to understand the students' profiles.

        Predictive Proposal: Create a predictive model to foresee student behavior based on some variables that may be crucial for identifying student development. In the predictive proposal, you can use creativity to propose a solution with a supervised or unsupervised algorithm. The idea is to use the knowledge learned in the course as a solution (machine learning, deep learning, or natural language processing).
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        ### Data Dictionary
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
            | Coluna | Descrição |
            |:----------------:|:-------------:|
            | INSTITUICAO_ENSINO_ALUNO_2020 | Mostra instituição de Ensino do Aluno em 2020 |
            | NOME | Nome do Aluno (dados estão anonimizados) |
            | IDADE_ALUNO_2020 | Idade do Aluno em 2020 |
            | PEDRA_2020 | Classificação do Aluno baseado no número do INDE (2020), o conceito de classificação é dado por: Quartzo – 2,405 a 5,506 / Ágata – 5,506 a 6,868 / Ametista – 6,868 a 8,230 / Topázio – 8,230 a 9,294 |
            | IAA_2020 | Indicador de Auto Avaliação – Média das Notas de Auto Avaliação do Aluno em 2020 |
            | IEG_2020 | Indicador de Engajamento – Média das Notas de Engajamento do Aluno em 2020 |
            | IPS_2020 | Indicador Psicossocial – Média das Notas Psicossociais do Aluno em 2020 |
            | IDA_2020 | Indicador de Aprendizagem - Média das Notas do Indicador de Aprendizagem 2020 |
            | IPP_2020 | Indicador Psicopedagógico – Média das Notas Psicopedagógicas do Aluno em 2020 |
            | IPV_2020 | Indicador de Ponto de Virada – Média das Notas de Ponto de Virada do Aluno em 2020 |
            | IAN_2020 | Indicador de Adequação ao Nível – Média das Notas de Adequação do Aluno ao nível atual em 2020 |
            | INDE_2020 | Índice do Desenvolvimento Educacional – Métrica de Processo Avaliativo Geral do Aluno, dado pela ponderação dos indicadores: IAN, IDA, IEG, IAA, IPS, IPP e IPV em 2020. |
            | DESTAQUE_IEG_2020 | Observações dos Avaliadores Sobre o Aluno referente ao "Indicador de Engajamento” em 2020 |
            | DESTAQUE_IDA_2020 | Observações dos Avaliadores Sobre o Aluno referente ao “Indicador de Aprendizagem” em 2020 |
            | DESTAQUE_IPV_2020 | Observações dos Avaliadores Sobre o Aluno referente ao “Indicador de Ponto de Virada” em 2020 |
            | PONTO_VIRADA_2020 | Campo do Tipo Booleano que sinaliza se o Aluno atingiu o “Ponto de Virada” em 2020 |
            | PEDRA_2021 | Classificação do Aluno baseado no número do INDE (2021), o conceito de classificação é dado por: Quartzo – 2,405 a 5,506 / Ágata – 5,506 a 6,868 / Ametista – 6,868 a 8,230 / Topázio – 8,230 a 9,294 |
            | IAA_2021 | Indicador de Auto Avaliação – Média das Notas de Auto Avaliação do Aluno em 2021 |
            | IEG_2021 | Indicador de Engajamento – Média das Notas de Engajamento do Aluno em 2021 |
            | IPS_2021 | Indicador Psicossocial – Média das Notas Psicossociais do Aluno em 2021 |
            | IDA_2021 | Indicador de Aprendizagem - Média das Notas do Indicador de Aprendizagem 2021 |
            | IPP_2021 | Indicador Psicopedagógico – Média das Notas Psicopedagógicas do Aluno em 2021 |
            | IPV_2021 | Indicador de Ponto de Virada – Média das Notas de Ponto de Virada do Aluno em 2021 |
            | IAN_2021 | Indicador de Adequação ao Nível – Média das Notas de Adequação do Aluno ao nível atual em 2021 |
            | INDE_2021 | Índice do Desenvolvimento Educacional – Métrica de Processo Avaliativo Geral do Aluno, dado pela ponderação dos indicadores: IAN, IDA, IEG, IAA, IPS, IPP e IPV em 2021. |
            | REC_EQUIPE_1_2021 | Recomendação: da Equipe de Avalição: 1 em 2021 |
            | REC_EQUIPE_2_2021 | Recomendação: da Equipe de Avalição: 2 em 2021 |
            | REC_EQUIPE_3_2021 | Recomendação: da Equipe de Avalição: 3 em 2021 |
            | REC_EQUIPE_4_2021 | Recomendação: da Equipe de Avalição: 3 em 2021 |
            | REC_PSICO_2021 | Mostra qual a recomendação da equipe de psicologia sobre o Aluno em 2021 |
            | PONTO_VIRADA_2021 | Campo do Tipo Booleano que sinaliza se o Aluno atingiu o “Ponto de Virada” em 2021 |
            | PEDRA_2022 | Classificação do Aluno baseado no número do INDE (2022), o conceito de classificação é dado por: Quartzo – 2,405 a 5,506 / Ágata – 5,506 a 6,868 / Ametista – 6,868 a 8,230 / Topázio – 8,230 a 9,294 |
            | IAA_2022 | Indicador de Auto Avaliação – Média das Notas de Auto Avaliação do Aluno em 2022 |
            | IEG_2022 | Indicador de Engajamento – Média das Notas de Engajamento do Aluno em 2022 |
            | IPS_2022 | Indicador Psicossocial – Média das Notas Psicossociais do Aluno em 2022 |
            | IDA_2022 | Indicador de Aprendizagem - Média das Notas do Indicador de Aprendizagem 2022 |
            | IPP_2022 | Indicador Psicopedagógico – Média das Notas Psicopedagógicas do Aluno em 2022 |
            | IPV_2022 | Indicador de Ponto de Virada – Média das Notas de Ponto de Virada do Aluno em 2022 |
            | IAN_2022 | Indicador de Adequação ao Nível – Média das Notas de Adequação do Aluno ao nível atual em 2022 |
            | INDE_2022 | Índice do Desenvolvimento Educacional – Métrica de Processo Avaliativo Geral do Aluno, dado pela ponderação dos indicadores: IAN, IDA, IEG, IAA, IPS, IPP e IPV em 2022. |
            | REC_PSICO_2022 | Mostra qual a recomendação da equipe de psicologia sobre o Aluno em 2022 |
            | REC_AVA_1_2022 | Recomendação da Equipe de Avalição 1 em 2022 |
            | REC_AVAL_2_2022 | Recomendação da Equipe de Avalição: 2 em 2022 |
            | REC_AVAL_3_2022 | Recomendação da Equipe de Avalição: 3 em 2022 |
            | REC_AVAL_4_2022 | Recomendação da Equipe de Avalição: 3 em 2022 |
            | DESTAQUE_IEG_2022 | Observações dos Mestres Sobre o Aluno referente ao "Indicador de Engajamento” em 2022 |
            | DESTAQUE_IDA_2022 | Observações dos Mestres Sobre o Aluno referente ao “Indicador de Aprendizagem” em 2022 |
            | DESTAQUE_IPV_2022 | Observações dos Mestres Sobre o Aluno referente ao “Indicador de Ponto de Virada” em 2022 |
            | PONTO_VIRADA_2022 | Campo do Tipo Booleano que sinaliza se o Aluno atingiu o “Ponto de Virada” em 2022 |
            | INDICADO_BOLSA_2022 | Campo do Tipo Booleano que sinaliza se o Aluno foi indicado para alguma Bolsa no Ano de 2022 |
        """,
        unsafe_allow_html=True,
    )

    # PassosMagicosSobreTab(tab0)
