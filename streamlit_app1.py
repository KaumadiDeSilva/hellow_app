import streamlit as st

st.title('Phishing Website Detection using Machine Learning')

st.write('This ML-based app is developed for educational purposes. Objective of the app is detecting phishing websites only using content data. Not URL!'
         ' You can see the details of approach, data set, and feature set if you click on _"See The Details"_. ')


         st.subheader('Data set')
         st.write('I used _"phishtank.org"_ & _"tranco-list.eu"_ as data sources.')
         st.write('Totally 26584 websites ==> **_16060_ legitimate** websites | **_10524_ phishing** websites')
         st.write('Data set was created in October 2022.')
      
