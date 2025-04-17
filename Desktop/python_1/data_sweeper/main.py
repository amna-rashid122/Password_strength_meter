import streamlit as st
import pandas as pd


st.title("🧹 Data Sweeper 🧼")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Original Data")
    st.write(df)

    # Simple cleaning example
    st.subheader("Cleaned Data")
    df_cleaned = df.drop_duplicates().dropna()
    st.write(df_cleaned)

    # Option to download cleaned data
    csv = df_cleaned.to_csv(index=False)
    st.download_button("Download Cleaned CSV", csv, file_name="cleaned_data.csv", mime="text/csv")
