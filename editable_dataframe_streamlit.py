import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect("data.db")
c = conn.cursor()
analyst = "Jed Gore"
portfolio_name = "Portfolio One"
ticker = "WMT"


@st.cache_data
def load_data():
    try:
        df = pd.read_sql_query("SELECT * from portfolios", conn)
    except:
        data = [["Test User", "WMT", "Portfolio One"]]
        df = pd.DataFrame(data, columns=["analyst", "ticker", "portfolio_name"])

    return df


@st.cache_data
def convert_df(df):
    return df.to_csv().encode("utf-8")


df = load_data()
edited_df = st.experimental_data_editor(df, num_rows="dynamic")


@st.cache_data
def convert_df(df):
    return df.to_csv(index=False).encode("utf-8")


csv = convert_df(edited_df)

if st.button("Save to SQL"):
    edited_df.to_sql("portfolios", conn, if_exists="replace")
    st.markdown("Saved")

st.download_button("Download to CSV", csv, "file.csv", "text/csv", key="download-csv")
