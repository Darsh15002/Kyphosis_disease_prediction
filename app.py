import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('randomtree.pkl','rb'))

def predict_disease(age, number,start):
    input = np.array([[age,number,start]]).astype(np.float64)
    prediction = model.predict(input)
    return prediction 

def main():
    html_temp = """"
    <div style='background-color:#025246; padding:10px'>
    <h2 style ='color:white;text-align:center;'>Kyhosis Disease Prediction Project</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    age = st.text_input("Age (in month)")
    number = st.text_input("Number")
    start = st.text_input("Start")

    danger_html="""  
      <div style="background-color:#F4D03F;padding:10px >
       <h2 style="color:white;text-align:center;font-size:30px;"> You are not suffering from Kyphosis disease.</h2>
       </div>
    """

    safe_html="""  
      <div style="background-color:#F08080;padding:10px >
       <h2 style="color:black ;text-align:center;font-size:30px;"> You are suffering from Kyphosis disease.</h2>
       </div>
    """
    if st.button("Predict"):
        output = predict_disease(age,number,start)
        st.success('Your Result is {}'.format(output))

        if output > 0:
            st.markdown(safe_html,unsafe_allow_html=True)
        else:
            st.markdown(danger_html,unsafe_allow_html=True)

if __name__=='__main__':
    main()
