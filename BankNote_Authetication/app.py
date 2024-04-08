import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image
from joblib import dump, load
#app=Flask(__name__)
#Swagger(app)


# final_model = open("model.joblib","rb")
# classifier = load('model.joblib')

classifier = load('model.joblib')

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(variance,skewness,curtosis,entropy):
    value = ''
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    if prediction ==0:
        value = 'Normal'
    else:
        value = 'Anomalous'
    return value



def main():
    st.title("Bank Authenticator")
    html_temp = """
<div style="background-color: tomato; padding: 20px; border-radius: 10px;">
    <h1 style="color: white; text-align: center; font-family: Arial, sans-serif;">Banknote Authenticator</h1>
    <p style="color: white; text-align: center; font-family: Arial, sans-serif;">Detect authenticity of banknotes using Machine Learning</p>
</div>
"""
    st.markdown(html_temp,unsafe_allow_html=True)
    variance = st.text_input("Variance","")
    if variance:
        try:
            variance_float = float(variance)
            if -20 <= variance_float <= 20:
                st.success('Valid Input')
            else:
                st.warning('Please enter values between -20 and 20 for variance.')
        except ValueError:
            st.warning('Not a valid input. Please enter valid number for variance.')
    else:
        try:
            pass
        except ValueError:
            st.warning('Variance cannot be empty.')

    skewness = st.text_input("skewness","")
    if skewness:
        try:
            skewness_float = float(skewness)
            if -20 <= skewness_float <= 20:
                st.success('Valid Input')
            else:
                st.warning('Please enter values between -20 and 20 for skewness.')
        except ValueError:
            st.warning('Not a valid input. Please enter valid number for skewness.')
    else:
        try:
            pass
        except ValueError:
            st.warning('Skewness cannot be empty.')
    curtosis = st.text_input("curtosis","")
    if curtosis:
        try:
            curtosis_float = float(curtosis)
            if -20 <= curtosis_float <= 20:
                st.success('Valid Input')
            else:
                st.warning('Please enter values between -20 and 20 for curtosis.')
        except ValueError:
            st.warning('Not a valid input. Please enter valid number for curtosis.')
    else:
        try:
            pass
        except ValueError:
            st.warning('Curtosis cannot be empty.')

    entropy = st.text_input("entropy","")
    if entropy:
        try:
            entropy_float = float(entropy)
            if -20 <= entropy_float <= 20:
                st.success('Valid Input')
            else:
                st.warning('Please enter values between -20 and 20 for entropy.')
        except ValueError:
            st.warning('Not a valid input. Please enter valid number for entropy.')
    else:
        try:
            pass
        except ValueError:
            st.warning('Entropy cannot be empty.')
    result=""
    if st.button("Predict"):
        try:
            result=predict_note_authentication(variance,skewness,curtosis,entropy)
            st.success('Bank Note Autentication predicts its  {}'.format(result))
        except ValueError:
            st.warning('Sorry, the inputs you entered are not correct, Please enter again')

    if st.button("About"):
        st.text("BankNote Authenticator ML App")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()