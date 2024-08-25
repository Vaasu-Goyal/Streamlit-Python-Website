import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Data Dashboard")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_box = st.selectbox("Select column to filter by", columns)
    unique_values = df[selected_box].unique()
    selected_value = st.selectbox("Select value to filter by", unique_values)

    # Filter the data based on selection
    filtered_df = df[df[selected_box] == selected_value]

    st.subheader("Filtered Data")
    st.write(filtered_df)

    st.subheader("Plot Data")
    x_column = st.selectbox("Select column for X-axis", columns)
    y_column = st.selectbox("Select column for Y-axis", columns)



    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])

else:
    st.write("Waiting on file upload...")

