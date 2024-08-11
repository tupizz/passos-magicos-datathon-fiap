import joblib
import streamlit as st
from keras.models import load_model
import plotly.graph_objs as go
import pandas as pd
import numpy as np

st.title('Scholarship Prediction Model')
st.markdown(
    """
    The scholarship prediction model uses a machine learning algorithm to predict whether a student is eligible to receive a scholarship based on their performance indicators.
    """
)

with st.container():
    model_path = "model/awarded_scholarship_model.pkl"
    scaler_path = "model/awarded_scholarship_scaler.pkl"

    # Load the model and scaler using joblib
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    epochs = np.array(range(2000))
    training = pd.read_csv(
        "model/model_training_data_hist.csv", sep=";"
    )

    st.success("Model and scaler loaded successfully.")

    st.markdown(
        f"""
        The scholarship recommendation model developed for the NGO **:green[Passos Mágicos]** was evaluated based on performance metrics, including loss and accuracy. The performance data shows that the model is generalizing well to unseen data, indicating that it does not suffer from *overfitting*.
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        The performance indicators used in the model are as follows:
        - **INDE**: Student's average grade in the last semester.
        - **IAN**: Number of classes attended by the student.
        - **IDA**: Student's average grade in the last year.
        - **IEG**: Number of classes the student participated in.
        - **IAA**: Number of classes the student passed.
        - **IPS**: Number of classes attended by the student.
        - **IPP**: Number of classes the student participated in.
        - **IPV**: Number of classes the student passed.
        """
    )

    with st.container():
        col0, col1 = st.columns(2)

        with col0:
            fig = go.Figure()

            fig.add_trace(
                go.Scatter(
                    x=epochs,
                    y=training["accuracy"],
                    mode="lines",
                    name="Traning Accuracy",
                    marker=dict(color='#90ee90')  # Set the color to light green
                )
            )
            fig.add_trace(
                go.Scatter(
                    x=epochs,
                    y=training["val_accuracy"],
                    mode="lines",
                    name="Validation Accuracy",
                    line=dict(color="red"),
                )
            )

            fig.update_layout(
                title="Performance (accuracy)",
                xaxis_title="Epochs",
                yaxis_title="Value",
                height=600,
                legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=1,
                ),
            )

            st.plotly_chart(fig, use_container_width=True)

        with col1:
            fig = go.Figure()

            fig.add_trace(
                go.Scatter(
                    x=epochs,
                    y=training["loss"],
                    mode="lines",
                    name="Loss of training",
                    marker=dict(color='#90ee90')  # Set the color to light green
                )
            )
            fig.add_trace(
                go.Scatter(
                    x=epochs,
                    y=training["val_loss"],
                    mode="lines",
                    name="Loss of Validation",
                    line=dict(color="red"),
                )
            )

            fig.update_layout(
                title="Performance (Loss)",
                xaxis_title="Epochs",
                yaxis_title="Value",
                height=600,
                legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=1,
                ),
            )

            st.plotly_chart(fig, use_container_width=True)


    st.markdown(
        """Use the controls below to simulate a student's performance indicators and click **:green[Predict]** to run the scholarship award model. This model provides **:green[2]** possible outcomes: recommend that the student **:green[receive]** a scholarship or **:green[not receive]** a scholarship."""
    )

    with st.container():
        col0, col1, col2, col3, col4, col5, col6, col7 = st.columns(8)


        with col0:
            indicator_inde = st.number_input(
                label="**:green[INDE]**",
                key="inde",
                min_value=0.0,
                max_value=10.0,
                value=0.0,
                step=0.1,
                format="%.2f",
            )

        with col1:
            indicator_ian = st.number_input(
                label="**:green[IAN]**",
                key="ian",
                min_value=0.0,
                max_value=10.0,
                value=0.0,
                step=0.1,
                format="%.2f",
            )

        with col2:
            indicator_ida = st.number_input(
                label="**:green[IDA]**",
                key="ida",
                min_value=0.0,
                max_value=10.0,
                value=0.0,
                step=0.1,
                format="%.2f",
            )

        with col3:
            indicator_ieg = st.number_input(
                label="**:green[IEG]**",
                key="ieg",
                min_value=0.0,
                max_value=10.0,
                value=0.0,
                step=0.1,
                format="%.2f",
            )

        with col4:
            indicator_iaa = st.number_input(
                label="**:green[IAA]**",
                key="iaa",
                min_value=0.0,
                max_value=10.0,
                value=0.0,
                step=0.1,
                format="%.2f",
            )

        with col5:
            indicator_ips = st.number_input(
                label="**:green[IPS]**",
                key="ips",
                min_value=0.0,
                max_value=10.0,
                value=0.0,
                step=0.1,
                format="%.2f",
            )

        with col6:
            indicator_ipp = st.number_input(
                label="**:green[IPP]**",
                key="ipp",
                min_value=0.0,
                max_value=10.0,
                value=0.0,
                step=0.1,
                format="%.2f",
            )

        with col7:
            indicator_ipv = st.number_input(
                label="**:green[IPV]**",
                key="ipv",
                min_value=0.0,
                max_value=10.0,
                value=0.0,
                step=0.1,
                format="%.2f",
            )

    student_data = pd.DataFrame(
        {
            "IAA": indicator_iaa,
            "IAN": indicator_ian,
            "IDA": indicator_ida,
            "IEG": indicator_ieg,
            "INDE": indicator_inde,
            "IPP": indicator_ipp,
            "IPS": indicator_ips,
            "IPV": indicator_ipv,
        },
        index=[0],
    )

    if st.button("⚡️ Predict", key="btn_predict_mlp"):
        with st.spinner("Processing..."):
            st.subheader(":green[Model Input Matrix]", divider="green")
            st.dataframe(student_data, hide_index=True)

            st.subheader(":green[Model Prediction]", divider="green")
            student_data_scaled = scaler.transform(student_data)
            prediction = model.predict(student_data_scaled)

            if prediction.round()[0] > 0:
                st.balloons()
                st.success(
                    ":white_check_mark: **Recommendation:** The student **is eligible** to receive the scholarship :grinning:"
                )
            else:
                st.error(
                    ":x: **Recommendation:** The student **is not eligible** to receive the scholarship :disappointed:"
                )
