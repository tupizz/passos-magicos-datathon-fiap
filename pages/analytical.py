import streamlit as st
import pandas as pd
import plotly.graph_objs as go
from utils.charts import (
    format_number,
    plot_boxplot,
    plot_histograma,
    plot_boxplot_analise_indicador,
    plot_boxplot_comparativo,
    classificar_distribuicao_histograma,
    plot_bar,
    plot_histograma_comparativo
)

# Load datasets
df_2020 = pd.read_csv("output/data_2020.csv", sep=";")
df_2021 = pd.read_csv("output/data_2021.csv", sep=";")
df_2022 = pd.read_csv("output/data_2022.csv", sep=";")
df_full = pd.read_csv("output/data_full.csv", sep=";")

# Title of the app
st.title('Analytics Dashboard')

with st.container():
    st.header("Exploratory Data Analysis (EDA)")

    # Format total counts
    total_original = format_number(len(df_full))
    total_2020 = format_number(len(df_2020))
    total_2021 = format_number(len(df_2021))
    total_2022 = format_number(len(df_2022))

    # Analysis of educational institutions
    st.subheader("Educational Institutions", divider="blue")
    st.markdown("""
    This section analyzes the educational institutions attended by students served by **Passos Mágicos**. 
    Note that data was provided only for **2020** and **2021**, so analysis for **2022** is not possible.
    """)

    # Educational institutions in 2020
    st.subheader("2020", divider="blue")
    fig = plot_bar(df_2020, "INSTITUICAO_ENSINO_ALUNO", "Educational Institutions of Students in 2020",
                   xaxis="Institution")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
        As shown in the chart above, the majority of students served by the NGO come from public schools. 
        This highlights the crucial role that **Passos Mágicos** plays in these students' lives, many of whom may lack access to quality education or state support. 
        Some students supported by the NGO have also gone on to attend institutions like **FIAP** or other higher education establishments, further demonstrating the organization's transformative impact.
        """)

    # Educational institutions in 2021
    st.subheader("2021", divider="blue")
    fig = plot_bar(df_2021, "INSTITUICAO_ENSINO_ALUNO", "Educational Institutions of Students in 2021",
                   xaxis="Institution")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
        Similar to the previous year, the majority of the children and youth served by the NGO in 2021 come from public schools.
        """)

    # Handle missing values in age
    df_2020["IDADE_ALUNO"] = pd.to_numeric(df_2020["IDADE_ALUNO"], errors="coerce")

    # Create age groups
    bins = [7, 10, 15, 21]
    labels = ["7-9", "10-14", "15+"]
    df_2020["FAIXA"] = pd.cut(df_2020["IDADE_ALUNO"], bins=bins, labels=labels, right=False)

    # Descriptive statistics for age
    col = "IDADE_ALUNO"
    df_descriptive = df_2020[col].describe().to_frame()
    df_descriptive.reset_index(inplace=True)
    df_descriptive.columns = ["Measure", "Age"]

    # Formatting descriptive stats for display
    measure_count = format_number(df_descriptive.loc[df_descriptive['Measure'] == 'count', 'Age'].values[0])
    measure_mean = format_number(df_descriptive.loc[df_descriptive['Measure'] == 'mean', 'Age'].values[0], "%0.2f")
    measure_std = format_number(df_descriptive.loc[df_descriptive['Measure'] == 'std', 'Age'].values[0])
    measure_min = format_number(df_descriptive.loc[df_descriptive['Measure'] == 'min', 'Age'].values[0])
    measure_25 = format_number(df_descriptive.loc[df_descriptive['Measure'] == '25%', 'Age'].values[0])
    measure_50 = format_number(df_descriptive.loc[df_descriptive['Measure'] == '50%', 'Age'].values[0])
    measure_75 = format_number(df_descriptive.loc[df_descriptive['Measure'] == '75%', 'Age'].values[0])
    measure_max = format_number(df_descriptive.loc[df_descriptive['Measure'] == 'max', 'Age'].values[0])

    st.markdown(f"""
    The table below provides a statistical overview of student ages for the year **2020**.
    With a total of **{measure_count}** observations, the average age is approximately **{measure_mean}** years, 
    with a standard deviation of **{measure_std}** years. The minimum recorded age is **{measure_min}** years, 
    and the maximum is **{measure_max}** years. Additionally, 25% of students are up to **{measure_25}** years old, 
    the median age is **{measure_50}** years, and 75% of students are up to **{measure_75}** years old.
    """)

    # Display the descriptive statistics table
    with st.container():
        _, col, _ = st.columns([3, 4, 3])
        with col:
            st.divider()
            st.dataframe(df_descriptive, use_container_width=True, hide_index=True)

    # Age distribution analysis
    st.subheader("Age Distribution", divider="blue")
    st.markdown("The following sections analyze the distribution of student ages for insightful patterns.")

    # Plot bar chart for age groups
    fig = plot_bar(df_2020, "IDADE_ALUNO", "Age of Students", xaxis="Age Group")
    st.plotly_chart(fig, use_container_width=True)

    # Calculate proportions for age groups
    total_students = len(df_2020)
    students_10_14 = len(df_2020.query("IDADE_ALUNO >= 10 & IDADE_ALUNO <= 14"))
    students_15plus = len(df_2020.query("IDADE_ALUNO >= 15"))
    proportion_10_14 = format_number(students_10_14 / total_students * 100, "%0.2f") + "%"
    proportion_15plus = format_number(students_15plus / total_students * 100, "%0.2f") + "%"

    st.markdown(f"""
    As seen in the above chart, a significant portion of students served by **Passos Mágicos** are aged between **10** and **14** years, 
    representing about **{proportion_10_14}** of the total. This suggests that the NGO's impact is greatest among children in the later stages of primary education. 
    Older students (**15+** years) are also supported by the NGO, but to a lesser extent, accounting for about **{proportion_15plus}** of the total.
    """)

    # Plot histogram for age distribution
    fig = plot_histograma(df_2020, "IDADE_ALUNO", "Distribution of Student Ages (%)", rug=False)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("The histogram above provides a clearer view of the percentage distribution of students by age, reaffirming that the 10-14 age group is the most represented.")


