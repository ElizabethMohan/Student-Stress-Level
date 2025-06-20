import streamlit as st
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to bottom, #0000ff, #000000);
        color: white;
    }
    html, body, [class*="css"]  {
        color: white;
    }
    .stTextInput > div > div > input,
    .stSelectbox > div > div > div > div,
    .stSlider > div > div > div {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🧠 Introduction to the Dataset")
st.markdown("""

The dataset titled “Student Stress Factors - A Comprehensive Analysis” provides a detailed exploration of various psychological, physiological, environmental, academic, and social factors contributing to stress levels among students.

It comprises multiple variables, each reflecting different dimensions of student life, such as:

Psychological issues (e.g., anxiety, self-esteem, depression)

Physiological symptoms (e.g., headaches, sleep quality)

Environmental safety & basic needs

Academic concerns (e.g., performance, future career pressure)

Social issues (e.g., bullying experiences)

Each entry is annotated with a stress level classification — ranging from no/mild stress, moderate stress, to high/severe stress — making it suitable for both statistical and machine learning-based analysis.
""")
st.title("📊 Overview of the Analysis")
st.markdown("""

This project aims to:

1. **Understand Key Stressors**
   Identify which categories (e.g., psychological or academic) contribute most to elevated stress levels.

2. **Visualize Correlations**
   Use heatmaps, histograms, and boxplots to visualize the relationship between individual factors and overall stress.

3. **Preprocess & Clean the Data**
   Handle missing values, scale features, and treat outliers (using techniques like capping instead of deletion).

4. **Build Predictive Models**
   Train a machine learning classifier (e.g., Naive Bayes) to predict a student's stress level based on their inputs.

5. **Deploy an Interactive Web App**
   Develop a user-friendly **Streamlit interface** where students can input their data and get real-time stress level predictions.

""")
st.title("Conclusion")
st.write("""
           The comprehensive analysis of the **Student Stress Factors** dataset has provided valuable insights into the various contributors to student stress. Through detailed **Exploratory Data Analysis (EDA)** and **Machine Learning-based Prediction**, we have identified key patterns and factors that significantly affect student well-being.

           ### Model Performance:

           - The Machine Learning model achieved an accuracy of **91%** in predicting student stress levels based on the provided features.
           - The model demonstrated good generalization on unseen data and provides a promising foundation for further refinement and application.

           """)
st.markdown("""
               ### 📚 Dataset Reference

               This analysis is based on the following dataset:

               👉 [Student Stress Factors - A Comprehensive Analysis (Kaggle)](https://www.kaggle.com/datasets/rxnach/student-stress-factors-a-comprehensive-analysis)
               """)

st.markdown("""
               ### Google Collab Link

               👉 [Open in Google Colab](https://colab.research.google.com/drive/1wos94FXXPruMNs3rjw-qbymTlTzLixhI#scrollTo=VXsUkzGtAPyn)
               """)
#Add About page to Streamlit app
