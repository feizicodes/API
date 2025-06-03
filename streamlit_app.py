import streamlit as st
import psycopg
import pandas as pd

def get_api_data():
    dbconn = st.secrets["DBCONN"]
    conn = psycopg.connect(dbconn)
    cur = conn.cursor()
    cur.execute("SELECT * FROM api_data;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return pd.DataFrame(rows, columns=["date", "open", "close"])

st.dataframe(get_api_data())

