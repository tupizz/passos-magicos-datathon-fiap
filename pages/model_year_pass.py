import joblib
import streamlit as st
import pandas as pd

# Setting the title of the Streamlit app
st.title('Next Grade Prediction Model')

# Loading the pre-trained model and scaler from disk using joblib
with st.container():
    model_path = "model/random_forest_ponto_virada_model.pkl"
    scaler_path = "model/random_forest_ponto_virada_scaler.pkl"

    # Load the model and scaler using joblib
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)

    st.success("Model and scaler loaded successfully. :)")

    # Providing a brief description of the app and the model it uses
    st.markdown(
        """
        This application leverages a machine learning model to predict whether a student is likely to advance to the next grade
        based on various performance indicators. The model is built using a random forest algorithm, which is known for its 
        robustness in classification tasks.
        """
    )

    # Explanation of how to use the controls and what the model predicts
    st.markdown(
        """Use the controls below to simulate a student's performance indicators and click **:blue[Predict]** to run the model. 
        This model predicts whether the student will pass to the next grade based on their performance. 
        The indicators used in the model are normalized using a scaler to ensure the model predictions are accurate."""
    )

    # Collecting input values for various student performance indicators from the user
    with st.container():
        col0, col1, col2, col3 = st.columns(4)

        # Collecting input for INDE indicator
        with col0:
            indicator_inde = st.number_input(
                label="**:blue[INDE]**",
                key="inde",
                min_value=0.0,
                max_value=10.0,
                value=0.0,
                step=0.1,
                format="%.2f",
            )

        # Collecting input for IAN indicator
        with col1:
            indicator_ian = st.number_input(
                label="**:blue[IAN]**",
                key="ian",
                min_value=0.0,
                max_value=10.0,
                value=0.0,
                step=0.1,
                format="%.2f",
            )

        # Collecting input for IDA indicator
        with col2:
            indicator_ida = st.number_input(
                label="**:blue[IDA]**",
                key="ida",
                min_value=0.0,
                max_value=10.0,
                value=0.0,
                step=0.1,
                format="%.2f",
            )

        # Collecting input for IEG indicator
        with col3:
            indicator_ieg = st.number_input(
                label="**:blue[IEG]**",
                key="ieg",
                min_value=0.0,
                max_value=10.0,
                value=0.0,
                step=0.1,
                format="%.2f",
            )

    # Collecting input for additional performance indicators
    with st.container():
        col0, col1, col2, col3 = st.columns(4)

        # Collecting input for IAA indicator
        with col0:
            indicator_iaa = st.number_input(
                label="**:blue[IAA]**",
                key="iaa",
                min_value=0.0,
                max_value=10.0,
                value=0.0,
                step=0.1,
                format="%.2f",
            )

        # Collecting input for IPS indicator
        with col1:
            indicator_ips = st.number_input(
                label="**:blue[IPS]**",
                key="ips",
                min_value=0.0,
                max_value=10.0,
                value=0.0,
                step=0.1,
                format="%.2f",
            )

        # Collecting input for IPP indicator
        with col2:
            indicator_ipp = st.number_input(
                label="**:blue[IPP]**",
                key="ipp",
                min_value=0.0,
                max_value=10.0,
                value=0.0,
                step=0.1,
                format="%.2f",
            )

        # Collecting input for IPV indicator
        with col3:
            indicator_ipv = st.number_input(
                label="**:blue[IPV]**",
                key="ipv",
                min_value=0.0,
                max_value=10.0,
                value=0.0,
                step=0.1,
                format="%.2f",
            )

    # Creating a DataFrame from the input values to feed into the model
    student_data = pd.DataFrame(
        {
            'IAA': indicator_iaa,
            'IEG': indicator_ieg,
            'IPS': indicator_ips,
            'IDA': indicator_ida,
            'IPP': indicator_ipp,
            'IPV': indicator_ipv,
            'IAN': indicator_ian,
            'INDE': indicator_inde
        },
        index=[0],
    )

    # Adding a button to trigger the model prediction
    if st.button("⚡️ Predict", key="btn_predict_mlp"):
        with st.spinner("Processing..."):
            st.subheader(":blue[Model Input Matrix]", divider="blue")
            st.dataframe(student_data, hide_index=True)

            st.subheader(":blue[Model Prediction]", divider="blue")

            # Scaling the input data using the loaded scaler
            student_data_scaled = scaler.transform(student_data)

            # Predicting whether the student will pass to the next grade using the pre-trained model
            prediction = model.predict(student_data_scaled)

            # Displaying the result of the prediction
            if prediction.round()[0] > 0:
                st.balloons()
                st.success(
                    ":white_check_mark: **Recommendation:** The student has a high probability of passing to the next grade :grinning:"
                )
            else:
                st.error(
                    ":x: **Recommendation:** The student has a low probability of passing to the next grade :disappointed:"
                )
