import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


word_to_number = {
"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
"five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
"ten": 10
}

def parse_number(word):
    return word_to_number.get(word.lower(), "Invalid number")

# Example usage
print(parse_number("one"))  # Output: 1
print(parse_number("five"))  # Output: 5

st.title("My First Streamlit App")
st.write("Hello, world! This is a simple Streamlit app.")

filepath = "sample.csv"
df = pd.read_csv(filepath)

st.write("### Data Preview")
st.dataframe(df)

num_required = 0
num_required_taken = 0
req_groups = {}
for row in df.itertuples():
    if row[5] == 'All':
        num_required += 1
        if row[6] == True:
            num_required_taken += 1
    elif row[4] not in req_groups:
        req_groups[row[4]] = parse_number(row[5])
        num_required += parse_number(row[5])
        if row[6] == True:
            num_required_taken += 1
            
pct_taken = (num_required_taken/num_required)*100
all_req = [pct_taken, 100-pct_taken]
labels = ["Classes taken", "Classes left"]


# Sample array data


st.title("Percent of degree completed:")

fig, ax = plt.subplots()
colors = ["#A52A2A", "#660000"]  # Light red, blue, green, and orange

ax.pie(all_req, labels=labels, colors=colors,autopct="%1.1f%%", startangle=90)
ax.axis("equal")  # Equal aspect ratio ensures pie is drawn as a circle.

st.pyplot(fig)


# # Show basic statistics
# st.write("### Basic Statistics")
# st.write(df.describe())

# # Allow user to select columns to display
# selected_columns = st.multiselect("Select columns to display", df.columns.tolist(), default=df.columns.tolist())

# # Display selected columns
# st.dataframe(df[selected_columns])

