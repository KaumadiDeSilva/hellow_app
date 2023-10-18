import streamlit as st

st.title('Phishing Website Detection using Machine Learning')
st.write('This ML-based app is developed for educational purposes. The objective of the app is to detect phishing websites using only content data, not the URL.'
         ' You can see the details of the approach, data set, and feature set if you click on _"See The Details"_. ')

with st.expander("PROJECT DETAILS"):
     st.subheader('Approach')
     st.write('I used _supervised learning_ to classify phishing and legitimate websites. '
             'I benefit from a content-based approach and focus on HTML of the websites. '
             'Also, I used scikit-learn for the ML models.')

     st.write('For this educational project, '
             'I created my own data set and defined features, some from the literature and some based on manual analysis. '
             'I used the requests library to collect data, BeautifulSoup module to parse and extract features.')

     st.write('The source code and data sets are available at the following GitHub link:')
     st.write('_https://github.com/emre-kocyigit/phishing-website-detection-content-based_')

st.subheader('Data set')
st.write('I used _"phishtank.org"_ & _"tranco-list.eu"_ as data sources.')
st.write('Totally 26584 websites ==> **_16060_ legitimate** websites | **_10524_ phishing** websites')
st.write('Data set was created in October 2022.')

# ----- FOR THE PIE CHART ----- #
labels = 'phishing', 'legitimate'
phishing_rate = int(ml.phishing_df.shape[0] / (ml.phishing_df.shape[0] + ml.legitimate_df.shape[0]) * 100)
legitimate_rate = 100 - phishing_rate
sizes = [phishing_rate, legitimate_rate]
explode = (0.1, 0)
fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, shadow=True, startangle=90, autopct='%1.1f%%')
ax.axis('equal')
st.pyplot(fig)
 # ----- !!!!! ----- #

