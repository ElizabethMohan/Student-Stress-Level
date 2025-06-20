import pickle
import streamlit as st
from PIL import Image
import numpy as np
import base64
st.markdown(
    """
    <style>
    .stApp {
        background-color:#000000;
        
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title(':blue[STUDENT STRESS LEVEL PREDICTION]')

def main():
    co1, co2 = st.columns([1, 2])
    with co1:
        img = Image.open('./mental.jpg')
        st.image(img, use_container_width=True)
    with co2:
        st.subheader(':blue[Psychological Factors]')
        anxiety = st.select_slider(":blue[Level of Anxiety issues]", options=[i for i in range(0, 21)])
        s_esteem = st.select_slider(":blue[Rate your Self esteem]", options=[i for i in range(0, 31)])
        depression = st.select_slider(":blue[Rate your level of depression related issues]", options=[i for i in range(0, 31)])

    co1, co2 = st.columns([1, 2])
    with co1:
        img = Image.open('./physical.jpg')
        st.image(img, use_container_width=True)
    with co2:
        st.subheader(':blue[Physiological Factors]')
        headache_options = ['Select an option', 'No headache', 'Rare', 'Occasional', 'Frequent', 'Very Frequent',
                            'Constant']
        headache_str = st.selectbox(":blue[Headache level]", options=headache_options)
        headache = headache_options.index(headache_str) - 1 if headache_str != 'Select an option' else None

        sleep = st.select_slider(":blue[Rate quality of your sleep]", options=[i for i in range(0, 6)])
    co1, co2 = st.columns([1, 2])

    with co1:
        img = Image.open('./education.jpg')
        st.image(img, use_container_width=True)
    with co2:
        st.subheader(':blue[Academic Factors]')
        academic_performance_options = ['Select an option', "Poor", "Below average", "Average", "Above average", "Good",
                                        "Excellent"]
        academic_performance_str = st.selectbox(":blue[Academic Performance]", options=academic_performance_options)
        academic_performance = academic_performance_options.index(
            academic_performance_str) - 1 if academic_performance_str != 'Select an option' else None

        future_career_concerns_options = ['Select an option', "No concern", "Very low concern", "Low concern",
                                          "Moderate concern", "High concern", "Very high concern"]
        future_career_concerns_str = st.selectbox(":blue[Future Career Concerns]",
                                                  options=future_career_concerns_options)
        future_career_concerns = future_career_concerns_options.index(
            future_career_concerns_str) - 1 if future_career_concerns_str != 'Select an option' else None

    co1, co2 = st.columns([1, 2])
    with co1:
        img = Image.open('./social.jpg')
        st.image(img, use_container_width=True)
    with co2:
        st.subheader(':blue[Social Factors]')
        bullying_options = ['Select an option', "No bullying experienced", "Very mild incidents",
                            "Occasional mild bullying", "Frequent moderate bullying", "Frequent severe bullying",
                            "Extreme / Persistent bullying"]
        bullying_str = st.selectbox(":blue[Bullying Experience Level]", options=bullying_options)
        bullying = bullying_options.index(bullying_str) - 1 if bullying_str != 'Select an option' else None

    features = [anxiety, s_esteem, depression, headache, sleep, safety, basic_needs, academic_performance,
    future_career_concerns, bullying]
    scaler = pickle.load(open('./minmax.sav', 'rb'))
    model= pickle.load(open('./modelsvc.sav', 'rb'))
    pred = st.button('Predict')
    stress = ['NO-MILD STRESS', 'MODETRATE STRESS', 'HIGH-SEVERE STRESS']

    if pred:
        result = model.predict(scaler.transform([features]))
        a = int(result[0])
        st.markdown(f"""
              <script>
              function closeModal() {{
                  document.getElementById('modal').style.display = 'none';
              }}
              </script>

              <div id="modal" style="
                  position: fixed;
                  top: 50%;
                  left: 50%;
                  background-color: #0000FF;
                  color: #000000;
                  padding: 20px;
                  border-radius: 10px;
                  box-shadow: 0 0 20px rgba(0,0,0,0.3);
                  z-index: 9999;
                  font-size: 24px;
                  font-weight: bold;
                  width: 30%;
                  text-align: center;
              ">
                  {stress[a]}
              </div>
              """, unsafe_allow_html=True)


main()


