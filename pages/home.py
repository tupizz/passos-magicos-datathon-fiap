import streamlit as st

# Custom CSS to style the table
st.markdown(
    """
    <style>
    .custom-table {
        width: 100%;
        border-collapse: collapse;
        margin: 25px 0;
        font-size: 18px;
        text-align: left;
    }
    .custom-table th, .custom-table td {
        padding: 12px 15px;
        border: 1px solid #e0e0e0;
        text-align: center;
    }
    .custom-table th {
        background-color: #fafafa; /* Soft light grey */
        color: #333333; /* Dark grey for contrast */
        font-weight: bold;
    }
    .custom-table tr:nth-child(even) {
        background-color: rgba(255,255,255,0.2); /* Very light grey for alternating rows */
    }
    .custom-table tr:hover {
        background-color: rgba(255,255,255,0.8); /* Slightly darker grey for hover effect */
        color: #333333; /* Dark grey for text on hover */
        transition: 0.3s; /* Smooth transition on hover */
        cursor: pointer; /* Cursor on hover */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Container to manage the layout of the page
with st.container():
    # Creating two columns, with a 7:3 ratio
    col0, col1 = st.columns([7, 3])

    # Adding a header in the first column
    with col0:
        st.header(f":orange[Passos Mágicos - Datathon FIAP {2024}]")

    # Adding a detailed markdown description about the Passos Mágicos Association
    st.markdown(
        """
        The Passos Mágicos Association has a 31-year history of working to transform the lives of low-income children and young people, helping them access better life opportunities.

        The transformation, envisioned by Michelle Flues and Dimetri Ivanoff, began in 1992, working within orphanages in the municipality of Embu-Guaçu.

        In 2016, after years of activity, they decided to expand the program so that more young people could have access to this magical formula for transformation, which includes: quality education, psychological/psychopedagogical support, broadening their worldview, and fostering leadership. They then began operating as a social and educational project, thus creating the Passos Mágicos Association.
        """,
        unsafe_allow_html=True,
    )

    # Explanation of the main objectives of the Datathon
    st.markdown(
        """
        ### Main Objective

        The main objective of the Datathon is for you, as a data scientist, to create a predictive proposal or, as a data analyst, to develop an analytical proposal to demonstrate the impact that the NGO "Passos Mágicos" has been making on the community it serves. The association seeks to empower the use of education as a tool for changing the living conditions of children and young people in social vulnerability. Based on the extensive research dataset on educational development from the period of 2020, 2021, and 2023, you can deliver one of the following proposals:

        Analytical Proposal: Create a storytelling to demonstrate the impacts that the NGO "Passos Mágicos" has had on student performance and raise performance indicators. The idea is to create a dashboard and storytelling by telling a story with the data to help Passos Mágicos make the best decisions based on the indicators and to understand the students' profiles.

        Predictive Proposal: Create a predictive model to foresee student behavior based on some variables that may be crucial for identifying student development. In the predictive proposal, you can use creativity to propose a solution with a supervised or unsupervised algorithm. The idea is to use the knowledge learned in the course as a solution (machine learning, deep learning, or natural language processing).
        """,
        unsafe_allow_html=True,
    )

    # Heading for the Data Dictionary section
    st.markdown(
        """
        ### Data Dictionary
        """,
        unsafe_allow_html=True,
    )

    # Creating the styled table using HTML
    st.markdown(
        f"""
        <table class="custom-table">
            <thead>
                <tr>
                    <th>Column</th>
                    <th>Description</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>INSTITUICAO_ENSINO_ALUNO_2020</td>
                    <td>Shows the student's educational institution in 2020</td>
                </tr>
                <tr>
                    <td>NOME</td>
                    <td>Student's name (data is anonymized)</td>
                </tr>
                <tr>
                    <td>IDADE_ALUNO_2020</td>
                    <td>Student's age in 2020</td>
                </tr>
                <tr>
                    <td>PEDRA_2020</td>
                    <td>Student's classification based on the INDE number (2020), the classification concept is given by: Quartz – 2.405 to 5.506 / Agate – 5.506 to 6.868 / Amethyst – 6.868 to 8.230 / Topaz – 8.230 to 9.294</td>
                </tr>
                <tr>
                    <td>IAA_2020</td>
                    <td>Self-Assessment Indicator – Average of the student's self-assessment scores in 2020</td>
                </tr>
                <tr>
                    <td>IEG_2020</td>
                    <td>Engagement Indicator – Average of the student's engagement scores in 2020</td>
                </tr>
                <tr>
                    <td>IPS_2020</td>
                    <td>Psychosocial Indicator – Average of the student's psychosocial scores in 2020</td>
                </tr>
                <tr>
                    <td>IDA_2020</td>
                    <td>Learning Indicator – Average of the student's learning indicator scores in 2020</td>
                </tr>
                <tr>
                    <td>IPP_2020</td>
                    <td>Psychopedagogical Indicator – Average of the student's psychopedagogical scores in 2020</td>
                </tr>
                <tr>
                    <td>IPV_2020</td>
                    <td>Turning Point Indicator – Average of the student's turning point scores in 2020</td>
                </tr>
                <tr>
                    <td>IAN_2020</td>
                    <td>Level Adequacy Indicator – Average of the student's adequacy scores to the current level in 2020</td>
                </tr>
                <tr>
                    <td>INDE_2020</td>
                    <td>Educational Development Index – Overall student evaluation process metric, given by the weighting of the indicators: IAN, IDA, IEG, IAA, IPS, IPP, and IPV in 2020.</td>
                </tr>
                <tr>
                    <td>DESTAQUE_IEG_2020</td>
                    <td>Evaluators' observations about the student regarding the "Engagement Indicator" in 2020</td>
                </tr>
                <tr>
                    <td>DESTAQUE_IDA_2020</td>
                    <td>Evaluators' observations about the student regarding the "Learning Indicator" in 2020</td>
                </tr>
                <tr>
                    <td>DESTAQUE_IPV_2020</td>
                    <td>Evaluators' observations about the student regarding the "Turning Point Indicator" in 2020</td>
                </tr>
                <tr>
                    <td>PONTO_VIRADA_2020</td>
                    <td>Boolean field indicating whether the student reached the "Turning Point" in 2020</td>
                </tr>
                <tr>
                    <td>PEDRA_2021</td>
                    <td>Student's classification based on the INDE number (2021), the classification concept is given by: Quartz – 2.405 to 5.506 / Agate – 5.506 to 6.868 / Amethyst – 6.868 to 8.230 / Topaz – 8.230 to 9.294</td>
                </tr>
                <tr>
                    <td>IAA_2021</td>
                    <td>Self-Assessment Indicator – Average of the student's self-assessment scores in 2021</td>
                </tr>
                <tr>
                    <td>IEG_2021</td>
                    <td>Engagement Indicator – Average of the student's engagement scores in 2021</td>
                </tr>
                <tr>
                    <td>IPS_2021</td>
                    <td>Psychosocial Indicator – Average of the student's psychosocial scores in 2021</td>
                </tr>
                <tr>
                    <td>IDA_2021</td>
                    <td>Learning Indicator – Average of the student's learning indicator scores in 2021</td>
                </tr>
                <tr>
                    <td>IPP_2021</td>
                    <td>Psychopedagogical Indicator – Average of the student's psychopedagogical scores in 2021</td>
                </tr>
                <tr>
                    <td>IPV_2021</td>
                    <td>Turning Point Indicator – Average of the student's turning point scores in 2021</td>
                </tr>
                <tr>
                    <td>IAN_2021</td>
                    <td>Level Adequacy Indicator – Average of the student's adequacy scores to the current level in 2021</td>
                </tr>
                <tr>
                    <td>INDE_2021</td>
                    <td>Educational Development Index – Overall student evaluation process metric, given by the weighting of the indicators: IAN, IDA, IEG, IAA, IPS, IPP, and IPV in 2021.</td>
                </tr>
                <tr>
                    <td>REC_EQUIPE_1_2021</td>
                    <td>Recommendation from the Evaluation Team: 1 in 2021</td>
                </tr>
                <tr>
                    <td>REC_EQUIPE_2_2021</td>
                    <td>Recommendation from the Evaluation Team: 2 in 2021</td>
                </tr>
                <tr>
                    <td>REC_EQUIPE_3_2021</td>
                    <td>Recommendation from the Evaluation Team: 3 in 2021</td>
                </tr>
                <tr>
                    <td>REC_EQUIPE_4_2021</td>
                    <td>Recommendation from the Evaluation Team: 4 in 2021</td>
                </tr>
                <tr>
                    <td>REC_PSICO_2021</td>
                    <td>Shows the recommendation from the psychology team about the student in 2021</td>
                </tr>
                <tr>
                    <td>PONTO_VIRADA_2021</td>
                    <td>Boolean field indicating whether the student reached the "Turning Point" in 2021</td>
                </tr>
                <tr>
                    <td>PEDRA_2022</td>
                    <td>Student's classification based on the INDE number (2022), the classification concept is given by: Quartz – 2.405 to 5.506 / Agate – 5.506 to 6.868 / Amethyst – 6.868 to 8.230 / Topaz – 8.230 to 9.294</td>
                </tr>
                <tr>
                    <td>IAA_2022</td>
                    <td>Self-Assessment Indicator – Average of the student's self-assessment scores in 2022</td>
                </tr>
                <tr>
                    <td>IEG_2022</td>
                    <td>Engagement Indicator – Average of the student's engagement scores in 2022</td>
                </tr>
                <tr>
                    <td>IPS_2022</td>
                    <td>Psychosocial Indicator – Average of the student's psychosocial scores in 2022</td>
                </tr>
                <tr>
                    <td>IDA_2022</td>
                    <td>Learning Indicator – Average of the student's learning indicator scores in 2022</td>
                </tr>
                <tr>
                    <td>IPP_2022</td>
                    <td>Psychopedagogical Indicator – Average of the student's psychopedagogical scores in 2022</td>
                </tr>
                <tr>
                    <td>IPV_2022</td>
                    <td>Turning Point Indicator – Average of the student's turning point scores in 2022</td>
                </tr>
                <tr>
                    <td>IAN_2022</td>
                    <td>Level Adequacy Indicator – Average of the student's adequacy scores to the current level in 2022</td>
                </tr>
                <tr>
                    <td>INDE_2022</td>
                    <td>Educational Development Index – Overall student evaluation process metric, given by the weighting of the indicators: IAN, IDA, IEG, IAA, IPS, IPP, and IPV in 2022.</td>
                </tr>
                <tr>
                    <td>REC_PSICO_2022</td>
                    <td>Shows the recommendation from the psychology team about the student in 2022</td>
                </tr>
                <tr>
                    <td>REC_AVA_1_2022</td>
                    <td>Recommendation from the Evaluation Team 1 in 2022</td>
                </tr>
                <tr>
                    <td>REC_AVAL_2_2022</td>
                    <td>Recommendation from the Evaluation Team: 2 in 2022</td>
                </tr>
                <tr>
                    <td>REC_AVAL_3_2022</td>
                    <td>Recommendation from the Evaluation Team: 3 in 2022</td>
                </tr>
                <tr>
                    <td>REC_AVAL_4_2022</td>
                    <td>Recommendation from the Evaluation Team: 4 in 2022</td>
                </tr>
                <tr>
                    <td>DESTAQUE_IEG_2022</td>
                    <td>Observations from the teachers about the student regarding the "Engagement Indicator" in 2022</td>
                </tr>
                <tr>
                    <td>DESTAQUE_IDA_2022</td>
                    <td>Observations from the teachers about the student regarding the "Learning Indicator" in 2022</td>
                </tr>
                <tr>
                    <td>DESTAQUE_IPV_2022</td>
                    <td>Observations from the teachers about the student regarding the "Turning Point Indicator" in 2022</td>
                </tr>
                <tr>
                    <td>PONTO_VIRADA_2022</td>
                    <td>Boolean field indicating whether the student reached the "Turning Point" in 2022</td>
                </tr>
                <tr>
                    <td>INDICADO_BOLSA_2022</td>
                    <td>Boolean field indicating whether the student was recommended for a scholarship in 2022</td>
                </tr>
            </tbody>
        </table>
        """,
        unsafe_allow_html=True
    )
