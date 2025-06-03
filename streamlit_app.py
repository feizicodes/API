
import streamlit as st
import psycopg
import pandas as pd



favourite_mentor = st.selectbox(
    "Who is your favourite CAB mentor?",
    ("Emily", "Muayad", "Raul", "Lucas", "Janina"),
    index=None,
    placeholder="Select your favourite mentor"
)

st.write("Your favourite mentor is: ", favourite_mentor)


def get_api_data():
  dbconn = st.secrets["DBCONN"]
  conn = psycopg.connect(dbconn)
  cur = conn.cursor()

  cur.execute('''
    SELECT * FROM api_data;
  ''')
  data = cur.fetchall()

  conn.commit()
  cur.close()
  conn.close()

  return pd.DataFrame(data, columns=["date", "open", "close"])

api_data = get_api_data()
st.dataframe(api_data)
