import os, pickle
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

# Set page config
st.set_page_config(page_title="Health Companion", layout="wide", page_icon="🚑", initial_sidebar_state="expanded")

# Get working dir
working_dir = os.path.dirname(os.path.abspath(__file__))

# Load models
diabetes_model = pickle.load(open( 'diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

# Diagnosis message function
@st.cache_data
def get_diagnosis_msg(prediction, disease):
    return f"❗ You may have {disease}." if prediction == 1 else f"💚 You're unlikely to have {disease}."

# Sidebar navigation
with st.sidebar:
    selected = option_menu('Disease Prediction', ['Diabetes', 'Heart Disease', 'Parkinson\'s'], icons=['activity', 'heart', 'person'], styles={"nav-link-selected": {"background-color": "#02ab21"}})

# Main content
if selected == 'Diabetes':
    st.title('🩺 Diabetes Prediction')
    cols = st.columns(3)
    with cols[0]:
        Pregnancies = st.number_input('Pregnancies', min_value=0, step=1)
        SkinThickness = st.number_input('Skin Thickness', min_value=0.0, step=0.1)
    with cols[1]:
        Glucose = st.number_input('Glucose Level', min_value=0.0, step=0.1)
        Insulin = st.number_input('Insulin Level', min_value=0.0, step=0.1)
    with cols[2]:
        BloodPressure = st.number_input('Blood Pressure', min_value=0.0, step=0.1)
        BMI = st.number_input('BMI', min_value=0.0, step=0.1)
    with cols[0]:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree', min_value=0.0, max_value=2.42, step=0.001)
    with cols[1]:
        Age = st.number_input('Age', min_value=0, step=1)

    if st.button("Predict"):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        diab_prediction = diabetes_model.predict([user_input])
        diagnosis_msg = get_diagnosis_msg(diab_prediction[0], 'diabetes')
        st.info(diagnosis_msg)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.header("🔍 About Diabetes")
    st.write("""
    Diabetes is a chronic condition characterized by high blood glucose levels due to the body's inability to produce or use insulin effectively. There are two main types:

    1. **Type 1 Diabetes**: The body's immune system attacks and destroys insulin-producing cells, requiring daily insulin injections or a pump.

    2. **Type 2 Diabetes**: The most common form, where the body becomes resistant to insulin or doesn't produce enough. It's often associated with obesity, inactivity, and an unhealthy diet.

    Early diagnosis and proper management are crucial to prevent complications like heart disease, stroke, kidney disease, nerve damage, and vision problems.

    Consult a healthcare professional for personalized advice and guidance.
    """)
    # image = Image.open('images.jpeg')
    # st.image(image, caption='Diabetes Awareness', use_column_width=True)

elif selected == 'Heart Disease':
    st.title('💓 Heart Disease Prediction')
    # ... (existing code for heart disease prediction)
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''


    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)
    st.markdown("<hr>", unsafe_allow_html=True)
    st.header("🔍 About Heart Disease")
    st.write("""
    **Heart disease**, also known as cardiovascular disease, refers to a group of disorders that affect the heart and blood vessels. It is a leading cause of death worldwide and can manifest in various forms, including:

    1. **Coronary Artery Disease (CAD)**: This is the most common type of heart disease, caused by a buildup of plaque in the arteries that supply blood to the heart muscle. Over time, this buildup can cause the arteries to narrow, reducing blood flow and potentially leading to a heart attack.

    2. **Heart Failure**: This condition occurs when the heart muscle is weakened and unable to pump blood effectively throughout the body. It can be caused by various factors, including CAD, high blood pressure, and other heart conditions.

    3. **Arrhythmia**: This refers to an abnormal heart rhythm, which can be too fast, too slow, or irregular. Arrhythmias can be caused by various factors, including heart disease, electrolyte imbalances, and certain medications.

    4. **Heart Valve Disorders**: These conditions involve problems with the heart valves, which regulate blood flow through the heart. Valve disorders can be congenital (present at birth) or acquired (developed later in life).

    Risk factors for heart disease include high blood pressure, high cholesterol levels, smoking, diabetes, obesity, lack of physical activity, and a family history of heart disease.

    Early detection and preventive measures, such as a healthy lifestyle and regular check-ups, are crucial in managing and reducing the risk of heart disease.
    """)     
    # image = Image.open('download.jpeg')
    # st.image(image, caption='Parkinson\'s Disease Awareness', use_column_width=True)

elif selected == "Parkinson's":
    st.title('🧠 Parkinson\'s Prediction')
    # ... (existing code for Parkinson's prediction)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
    st.markdown("<hr>", unsafe_allow_html=True)
    st.header("🔍 About Parkinson's Disease")
    st.write("""
    **Parkinson's disease** is a progressive neurological disorder that affects movement. It occurs when nerve cells (neurons) in the brain responsible for producing dopamine, a chemical messenger that helps control movement, become impaired or die.

    The main symptoms of Parkinson's disease include:

    1. **Tremors**: Involuntary shaking or trembling, often starting in one hand or arm and eventually affecting other limbs.

    2. **Bradykinesia**: Slowness of movement, which can make simple tasks like walking or getting dressed difficult.

    3. **Rigid Muscles**: Stiffness or rigidity in the limbs and trunk, which can limit movement and cause pain.

    4. **Postural Instability**: Impaired balance and coordination, increasing the risk of falls.

    5. **Non-Motor Symptoms**: In addition to movement-related symptoms, Parkinson's disease can also cause non-motor symptoms like sleep disturbances, cognitive changes, depression, and constipation.

    While the exact cause of Parkinson's disease is unknown, it is believed to be a combination of genetic and environmental factors. The risk increases with age, but it can also occur in younger individuals.

    There is no cure for Parkinson's disease, but treatments are available to manage the symptoms and improve quality of life. Early diagnosis and proper management, including medication, physical therapy, and lifestyle modifications, are crucial in slowing the progression of the disease.
    """)
    # image = Image.open('images (1).jpeg') 
    # st.image(image, caption='Parkinson\'s Disease Awareness', use_column_width=True)
    

if __name__ == "__main__":
    st.sidebar.markdown("""
    <h3 style='text-align: center; color: #02ab21;'>Health Companion</h3>
    <p style='text-align: center;'>Your journey to wellness starts here.</p>
    """, unsafe_allow_html=True)
    # st.sidebar.image('images.png', use_column_width=True)
