
import streamlit as t
import joblib

t.set_page_config(
          page_title="Sentiment Analyzer",
          page_icon="🎭")


co = joblib.load('v')
mo = joblib.load('model')

t.title('Sentiment Analysis')
t.write("An App created by me to analyze people's sentiment.\n\n"
          "DISCLAIMER: THIS IS JUST A PRELIMINARY EXPERIMENT, TRAINING DATA IS TOO LOW TO BE OF ANY USE IN PRACTICAL ENVIRONMENT.\n"
           "ALSO, THE APP CAN ONLY PREDICT TWO EMOTION: POSITIVE OR NEGATIVE.")

t.divider()


text = t.text_area('Enter your sentence: ')

if t.button('Analyse'):
    b = co.transform([text])
    p = mo.predict(b)

    if p[0] == 1:
        t.success("😊 Pos")
    else:
        t.error('😞 Negative')
