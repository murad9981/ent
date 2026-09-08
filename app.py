
import streamlit as t
import joblib

co = joblib.load('v')
mo = joblib.load('model')

t.title('Sentiment Analysis')
t.write("An App created by me to analyze people's sentiment.\n\n"
          'DISCLAIMER: THIS IS JUST A PRELIMINARY EXPERIMENT, TRAINING DATA IS TOO LOW TO BE OF ANY USE IN PRACTICAL ENVIRONMENT.')

text = t.text_area('enter your sentence: ')

if t.button('Analyse'):
    b = co.transform([text])
    p = mo.predict(b)

    if p[0] == 1:
        t.write('😊 Positive')
    else:
        t.write('😞 Negative')
