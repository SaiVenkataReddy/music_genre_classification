import streamlit as st

st.header("Music Genre Classification using ML and Deep Learning Techniques")
with st.form("Provide Input and Select Model to Predict the Genre"):
   st.write("Input music and select model name required")
   audio=st.file_uploader("Input music file for classification", type=['wav'])
   model = st.selectbox(
       'ML model to predict genre for given input:',
       ('KNN', 'Logistic Regression', 'SVM', 'CNN'))

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")



if submitted:
    st.write("Results Generated are")
    with st.spinner('Running the simulation. Please wait...'):
        for i in range(100000):
            x=1
    st.success('Done!')
    st.write(f"Input audio file is {audio} and Selected model is {model}")
    st.audio(audio, format="audio/wav")