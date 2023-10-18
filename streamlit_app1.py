import streamlit as st
import machine_learning as ml
import feature_extraction as fe
from bs4 import BeautifulSoup
import requests as re
import matplotlib.pyplot as plt

st.title('Phishing Website Detection using Machine Learning')

st.write('This ML-based app is developed for educational purposes. The objective of the app is to detect phishing websites using only content data, not the URL.'
         ' You can see the details of the approach, data set, and feature set if you click on _"See The Details"_. ')

st.subheader('Data set')
st.write('I used _"phishtank.org"_ & _"tranco-list.eu"_ as data sources.')
st.write('Totally 26584 websites ==> **_16060_ legitimate** websites | **_10524_ phishing** websites')
st.write('The data set was created in October 2022.')

