import streamlit as st


st.title('Phishing Website Detection using Machine Learning')

st.write('This ML-based app is developed for educational purposes. The objective of the app is to detect phishing websites using only content data, not the URL.'
         ' You can see the details of the approach, data set, and feature set if you click on _"See The Details"_. ')

st.title('Phishing Website Detection using Machine Learning')
st.write('This ML-based app is developed for educational purposes. Objective of the app is detecting phishing websites only using content data. Not URL!'
         ' You can see the details of approach, data set, and feature set if you click on _"See The Details"_. ')


with st.expander("PROJECT DETAILS"):
     st.subheader('Approach')
     st.write('I used _supervised learning_ to classify phishing and legitimate websites. '
             'I benefit from content-based approach and focus on html of the websites. '
             'Also, I used scikit-learn for the ML models.'
             )
