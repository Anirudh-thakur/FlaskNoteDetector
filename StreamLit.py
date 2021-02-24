#from flask import Flask,request
import pandas as pd 
import numpy as np
import pickle
#from flasgger import Swagger
import streamlit as st

#app=Flask(__name__)
#app.run(host='0.0.0.0')
#Swagger(app)
pickle_in = open('classifier.pkl','rb')
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"


#@app.route('/predict', methods=["Get"])
def predict_note_authentication(variance,skewness,curtosis,entropy):
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
    return "The predicted value is "+ str(prediction)


def main():
    st.title("Bank Authentication")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style ="color:white;text-align:center">StreamLit Bank Authentication API</h2>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance = st.text_input("Variance","Type here")
    skewness  = st.text_input("Skewness","Type here")
    curtosis = st.text_input("Curtosis","Type here")
    entropy = st.text_input("Entropy","Type here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(variance,skewness,curtosis,entropy)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets Learn")
        st.text("Built with Streamlit by Anirudh Thakur")
if __name__ == "__main__":
    main()

