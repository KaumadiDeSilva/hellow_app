import streamlit as st

st.title('Phishing Website Detection using Machine Learning')

st.write('This ML-based app is developed for educational purposes. Objective of the app is detecting phishing websites only using content data. Not URL!'
         ' You can see the details of approach, data set, and feature set if you click on _"See The Details"_. ')

with st.echo('approach'):
         I used supervised learning to classify phishing and legitimate websites. I benefit from content-based approach and focus on html of the websites. Also, I used scikit-learn for the ML models.


      
