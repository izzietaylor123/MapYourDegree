import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from app.nav import SideBarLinks
from web_scraping import get_courses

SideBarLinks()

word_to_number = {
"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
"five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
"ten": 10
}

def parse_number(word):
    return word_to_number.get(word.lower(), "Invalid number")

url = st.session_state['url'][0]

degree = st.session_state['degree'][0]

major_degree = degree.split(",")
major = major_degree[0].strip()
st.title(f"Course requirements for: ***{degree}***")
st.write("-----------------------------------------")
major = major.replace(" ", "-")
degree = major_degree[1].strip()

csv_list = get_courses(url, major, degree)
i = 0
concentrations = {}
for file in csv_list:
    name = file.split("-")[-1].split(".")[0]
    if "Concentration" in name:
        concentrations[name] = f"{file}"
    else :
        i += 1
        filepath = f"{file}"
        df = pd.read_csv(filepath)

        reqs_df = pd.read_csv(filepath)

        st.write(f"**{name}**")
        # Display editable checkbox column
        edited_df = st.data_editor(
            reqs_df,
            column_config={
                "Completed": st.column_config.CheckboxColumn("Completed"),
            },
            use_container_width=True
        )

        # Button to save changes
        if st.button("Save Changes", key = i):
            i += 1
            num_required = 0
            num_required_taken = 0
            req_groups = {} # req_group : num required, satisfied
            for row in edited_df.itertuples():
                if row[5] == 'All':
                    num_required += 1
                    if row[6] == True:
                        num_required_taken += 1
                elif row[4] not in req_groups:
                    req_groups[row[4]] = [parse_number(row[5]), False]
                    num_required += parse_number(row[5])
                    if row[6] == True:
                        num_required_taken += 1
                        req_groups[row[4]][0] -=1
                        if req_groups[row[4]][0] == 0:
                            req_groups[row[4]][1] = True
                elif req_groups[row[4]][1] == False:
                    if row[6] == True:
                        num_required_taken += 1
                        req_groups[row[4]][0] -=1
                        if req_groups[row[4]][0] == 0:
                            req_groups[row[4]][1] = True


            pct_taken = (num_required_taken/num_required)*100
            all_req = [pct_taken, 100-pct_taken]
            labels = ["Classes taken", "Classes left"]        

            st.subheader(f"**Percent of ***{name}*** completed:**")

            fig, ax = plt.subplots()
            colors = ["#A52A2A", "#660000"]  # Light red, blue, green, and orange
            fig.set_facecolor('#f7c3c3')
            ax.pie(all_req, labels=labels, colors=colors,autopct="%1.1f%%", startangle=90, textprops={'color': 'white'})
            ax.axis("equal")  # Equal aspect ratio ensures pie is drawn as a circle.

            st.pyplot(fig)

if len(concentrations) > 0:
    options = concentrations.keys()
    selection = st.pills("Choose a concentration:", options, selection_mode="single")
    if selection:
        st.markdown(f"Your selected option: {selection}.")
        
        concentrations_df = pd.read_csv(concentrations[f"{selection}"])

        # Display editable checkbox column
        edited_df = st.data_editor(
            concentrations_df,
            column_config={
                "Completed": st.column_config.CheckboxColumn("Completed"),
            },
            use_container_width=True
        )
        i += 1
        # Button to save changes
        if st.button("Save Changes", key = i):
            i += 1

            num_required = 0
            num_required_taken = 0
            req_groups = {} # req_group : num required, satisfied
            for row in edited_df.itertuples():
                if row[5] == 'All':
                    num_required += 1
                    if row[6] == True:
                        num_required_taken += 1
                elif row[4] not in req_groups:
                    req_groups[row[4]] = [parse_number(row[5]), False]
                    num_required += parse_number(row[5])
                    if row[6] == True:
                        num_required_taken += 1
                        req_groups[row[4]][0] -=1
                        if req_groups[row[4]][0] == 0:
                            req_groups[row[4]][1] = True
                elif req_groups[row[4]][1] == False:
                    if row[6] == True:
                        num_required_taken += 1
                        req_groups[row[4]][0] -=1
                        if req_groups[row[4]][0] == 0:
                            req_groups[row[4]][1] = True

            pct_taken = (num_required_taken/num_required)*100
            all_req = [pct_taken, 100-pct_taken]
            labels = ["Classes taken", "Classes left"]       
            st.subheader(f"**Percent of :red[{selection}] completed:**")

            fig, ax = plt.subplots()
            colors = ["#A52A2A", "#660000"]  # Light red, blue, green, and orange

            ax.pie(all_req, labels=labels, colors=colors,autopct="%1.1f%%", startangle=90)
            ax.axis("equal")  # Equal aspect ratio ensures pie is drawn as a circle.

            st.pyplot(fig)