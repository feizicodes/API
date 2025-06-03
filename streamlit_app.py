

import streamlit as st
import psycopg
import pandas as pd

st.write("Secrets keys:", st.secrets.keys())
def get_api_data():
    dbconn = st.secrets["DBCONN"]
    conn = psycopg.connect(dbconn)
    cur = conn.cursor()

    cur.execute('SELECT * FROM api_data;')
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return pd.DataFrame(rows, columns=["date", "open", "close"])

api_data = get_api_data()
st.dataframe(api_data)