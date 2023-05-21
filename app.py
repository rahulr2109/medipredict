# This file consist of streamlit app template

# importing necessary modules
import streamlit as st 
import joblib
import pandas as pd
import time

# Set the page config to wide mode
st.set_page_config(layout="wide")



# loading model and list of symptoms
model = joblib.load("saved_model/random_f.joblib")
symptoms_list = ['itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills', 'joint_pain', 'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition', 'spotting_ urination', 'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness', 'lethargy', 'patches_in_throat', 'irregular_sugar_level', 'cough', 'high_fever', 'sunken_eyes', 'breathlessness', 'sweating', 'dehydration', 'indigestion', 'headache', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine', 'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs', 'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips', 'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints', 'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine', 'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain', 'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum', 'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen', 'history_of_alcohol_consumption', 'fluid_overload.1', 'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose', 'yellow_crust_ooze']

# start of streamlit UI

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
st.markdown('<link rel="stylesheet" href="css/navcss.css">' , unsafe_allow_html=True)

navbar="""<nav
  class="navbar navbar-expand-lg navbar-light bg-light"
  style="
    box-shadow: #74c52b 0px 1px 2px 0px, rgba(60, 64, 67, 0.15) 0px 2px 6px 2px;
    position: sticky;
  "
>
  <a
    class="navbar-brand"
    href="/index"
    style="color: #74c52b; letter-spacing: 0.3em"
  >
    <img
      src="/assets/img/smallLogo.png"
      width="60"
      height="60"
      class="d-inline-block align-top img-fluid"
      style="position: fixed; top: 0"
      alt=""
      id="rotateIcon"
    />
    <span style="margin-left: 4em; margin-right: 0em"> MEDI-MATCH </span>
  </a>
  <button
    class="navbar-toggler"
    type="button"
    data-toggle="collapse"
    data-target="#navbarNavDropdown"
    aria-controls="navbarNavDropdown"
    aria-expanded="false"
    aria-label="Toggle navigation"
  >
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNavDropdown">
    <ul class="navbar-nav" style="padding-left: 2em">
      <li class="nav-item">
        <a class="nav-link" href="/index"
          >HOME <span class="sr-only">(current)</span></a
        >
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/doctors">DOCTORS</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/gallery">GALLERY</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/about">ABOUT US</a>
      </li>
    </ul>
    <div class="navbar-nav ml-auto" style="padding-left: 2em">
      <a class="nav-link" href="#">REGISTER</a>
      <a class="nav-link" href="#">LOG IN</a>
      <a class="nav-link" href="#">LOG OUT</a>
    </div>
  </div>
</nav>
"""

st.markdown(navbar,unsafe_allow_html=True)



st.title("Medi-Detect : The Smart health predictor")
st.header("Please enter your symptoms 🩺")

symptoms = st.multiselect('Enter your symptoms so that we can get you a primary diagnosis:',[*symptoms_list],key='symptoms')

# creating dataframe for accepting testing values
prediction_value = [0 for i in range(132)]
for sym in symptoms:
    index = symptoms_list.index(sym)
    # assigning encoded value to testing frame
    prediction_value[index] = 1

# convert list to Pandas dataframe and transpose it for model evaluation
query = pd.DataFrame(prediction_value).T
prediction = model.predict(query)

# evaluation and confirmation
if st.button("Evaluate"):
    with st.spinner('Predicting output...'):
        time.sleep(1)
        if symptoms:
            st.success("Prediction complete!")
            st.write("The diagnosis we have reached is: ")
            st.error(*prediction)
            st.write("Please consult your nearest health administrator soon, take care! 🏥")
            
        else:
            st.info("Please enter at least one symptom before clicking evaluate!")
#footer-----
footer="""<hr><!--=== Footer ===-->
<div class="footer-basic" data-aos="slide-up">
<center>
    <footer>
        <div class="social"><a href="#"><i class="icon ion-social-instagram"></i></a><a href="#"><i class="icon ion-social-snapchat"></i></a><a href="#"><i class="icon ion-social-twitter"></i></a><a href="#"><i class="icon ion-social-facebook"></i></a></div>
        <ul class="list-inline">
            <li class="list-inline-item"><a href="#">Home</a></li>
            <li class="list-inline-item"><a href="#">Services</a></li>
            <li class="list-inline-item"><a href="#">About</a></li>
            <li class="list-inline-item"><a href="#">Terms</a></li>
            <li class="list-inline-item"><a href="#">Privacy Policy</a></li>
        </ul>
    </footer>
    <p class="copyright">Medi-Match Hospital © 2023</p>
</center>
</div>
  <!--=== End Footer ===-->
"""
st.markdown('<link rel="stylesheet" href="css/footer.css">' , unsafe_allow_html=True)
st.markdown('<link rel="stylesheet" href="css/footer_01.css">' , unsafe_allow_html=True)

st.markdown(footer,unsafe_allow_html=True)            

        
        