import joblib
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objs as go


# Setting the title of the Streamlit app
st.title('Next Grade Prediction Model')

# Loading the pre-trained model and scaler from disk using joblib
with st.container():
    model_path = "model/random_forest_ponto_virada_model.pkl"
    scaler_path = "model/random_forest_ponto_virada_scaler.pkl"
    feature_importance_df = pd.read_csv(
        "output/ponto_virada_feature_importance.csv", sep=","
    )

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

    st.markdown(
        """
        Reasons why I have chosen the Random Forest model:
        - **Interpretability**: Random Forest models are easy to interpret and understand.
        - **Feature Importance**: Random Forest models provide feature importance, which helps in understanding the impact of each feature on the prediction.
        - **Robustness**: Random Forest models are robust to overfitting and noise in the data.
        - **Non-linear relationships**: Random Forest models can capture non-linear relationships between features and the target variable.
        - **Handles Missing Data and Imbalanced Datasets**: Random Forest models can handle missing data and imbalanced datasets effectively. It can be tuned with class weights or combined with techniques like SMOTE to handle imbalanced classes 
        """
    )

    st.markdown(
        """
        The performance indicators used in the model are as follows:
        - **IAN**: Student's average grade in the last semester.
        - **IPV**: Number of classes attended by the student.
        - **IAA**: Student's average grade in the last year.
        - **IPS**: Number of classes the student participated in.
        - **IPP**: Number of classes the student passed.
        """
    )

    st.markdown(
        """
        The feature importance plot below shows the importance of each feature in the model. The higher the value, the more important the feature is in predicting the student's grade advancement.
        """
    )

    with st.container():

        # Plot using Plotly
        fig = go.Figure()

        fig.add_trace(
            go.Bar(
                x=feature_importance_df['Importance'],
                y=feature_importance_df['Feature'],
                orientation='h',
                marker=dict(color='#90ee90'),  # Set the color to light green
                name="Feature Importance",
            )
        )

        fig.update_layout(
            title="Feature Importance in Random Forest Model",
            xaxis_title="Importance",
            yaxis_title="Feature",
            yaxis=dict(
                autorange="reversed"  # To invert y-axis like plt.gca().invert_yaxis()
            ),
            height=600,
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1,
            ),
        )

        # Display the plot in Streamlit
        st.plotly_chart(fig)

    # Collecting input values for various student performance indicators from the user
    with st.container():
        col0, col1, col2, col3, col4 = st.columns(5)

        # Collecting input for IAN indicator
        with col0:
            indicator_ian = st.number_input(
                label="**:green[IAN]**",
                key="ian",
                min_value=0.0,
                max_value=10.0,
                value=0.0,
                step=0.1,
                format="%.2f",
            )

        # Collecting input for IPV indicator
        with col1:
            indicator_ipv = st.number_input(
                label="**:green[IPV]**",
                key="ipv",
                min_value=0.0,
                max_value=10.0,
                value=0.0,
                step=0.1,
                format="%.2f",
            )

        # Collecting input for IAA indicator
        with col2:
            indicator_iaa = st.number_input(
                label="**:green[IAA]**",
                key="iaa",
                min_value=0.0,
                max_value=10.0,
                value=0.0,
                step=0.1,
                format="%.2f",
            )


        # Collecting input for IPS indicator
        with col3:
            indicator_ips = st.number_input(
                label="**:green[IPS]**",
                key="ips",
                min_value=0.0,
                max_value=10.0,
                value=0.0,
                step=0.1,
                format="%.2f",
            )

        # Collecting input for IPP indicator
        with col4:
            indicator_ipp = st.number_input(
                label="**:green[IPP]**",
                key="ipp",
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
            'IPS': indicator_ips,
            'IPP': indicator_ipp,
            'IPV': indicator_ipv,
            'IAN': indicator_ian,
        },
        index=[0],
    )

    # Adding a button to trigger the model prediction
    if st.button("⚡️ Predict", key="btn_predict_mlp"):
        with st.spinner("Processing..."):
            st.subheader(":green[Model Input Matrix]", divider="green")
            st.dataframe(student_data, hide_index=True)

            st.subheader(":green[Model Prediction]", divider="green")

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
