import streamlit as st
import pandas as pd

st.title("My First Streamlit App")
st.write("Hello, world! This is a simple Streamlit app.")

filepath = "sample.csv"
df = pd.read_csv(filepath)

st.write("### Data Preview")
st.dataframe(df)



# # Show basic statistics
# st.write("### Basic Statistics")
# st.write(df.describe())

# # Allow user to select columns to display
# selected_columns = st.multiselect("Select columns to display", df.columns.tolist(), default=df.columns.tolist())

# # Display selected columns
# st.dataframe(df[selected_columns])