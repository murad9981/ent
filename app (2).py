
import streamlit as t
import joblib

co = joblib.load('v')
mo = joblib.load('model')

t.title('sentiment_analysis')

text = t.text_input('enter your sentence: ')

if t.button('Analyse'):
    b = co.transform([text])
    p = mo.predict(b)

    if p[0] == 1:
        t.write('pos')
    else:
        t.write('neg')
