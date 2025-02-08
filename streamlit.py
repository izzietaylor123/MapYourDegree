import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import csv


word_to_number = {
"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
"five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
"ten": 10
}

def parse_number(word):
    return word_to_number.get(word.lower(), "Invalid number")

def get_title(url):
    # Send HTTP request
    response = requests.get(url)

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract the full title
    title = soup.title.string

    # Split the title to get the first part ("Computer Science")
    title_parts = title.split("<")
    main_title = title_parts[0].strip()  # Remove any leading/trailing spaces

    # Print the extracted title
    print(main_title)

    # Print the extracted title
    return (main_title)

def get_courses(url, major, degree):

    # Step 1: Fetch the catalog page
    url = f"{url}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    csv_list = []
    
    # Step 2: Find all tbody elements

    # Find all tables with the class "sc_courselist"
    tables = soup.find_all("table", class_="sc_courselist")

    all_h3_elements = []
    for table in tables:
        current_group = "Default"
        num_required = "All"
        # Get all preceding siblings of the table
        preceding_siblings = []
        current_sibling = table.previous_sibling
        while current_sibling:
            if current_sibling.name:
                preceding_siblings.append(current_sibling)
            current_sibling = current_sibling.previous_sibling

        # Reverse the list to maintain the correct order
        preceding_siblings.reverse()

        # Extract h3 elements from the preceding siblings
        h3_elements = [sibling for sibling in preceding_siblings if (sibling.name == "h3" or sibling.name == "h2")]
        all_h3_elements.extend(h3_elements)
        rows = table.find_all("tr")
        courses = []
        for row in rows:
            # Check if row contains a requirement group header
            # comment_td = row.find("td", colspan="2")
            # print(f"comment: {comment_td}")
            # if comment_td:
            requirement_group = row.find("span", class_="courselistcomment areaheader")

            if requirement_group:
                current_group = requirement_group.text.strip()
            comment_span = row.find("span", class_="courselistcomment")
            if comment_span:
                if ("Complete" in comment_span.text):
                    index = comment_span.text.split(" ").index("Complete")
                    num_required = comment_span.text.split(" ")[index+1]
                    if "Default" in current_group:
                        current_group = current_group + "1"
            # Skip section headers
            if "areaheader" in row.get("class", []):
                continue

            # Extract course information
            td_elements = row.find_all("td")
            if (len(td_elements) >= 3 or (len(td_elements) == 2 and "or" in td_elements[0].text)):

                # if "areasubheader" in td_elements[0].get('class'):
                course_code = td_elements[0].text.strip()
                if "and" in course_code:
                    course_code = course_code.replace('\n', '')
                    course_code = ' '.join(course_code.split())
                course_name = td_elements[1].text.strip()
                if "and" in course_name:
                    course_name = course_name.replace('\n', '')
                    course_name = ' '.join(course_name.split())
                course_hours = ""
                if len(td_elements) > 2:
                    course_hours = td_elements[2].text.strip()

                courses.append([course_code, course_name, course_hours, current_group, num_required, False])
        title = "Core"
        if all_h3_elements:
            title = all_h3_elements[-1].text
        # Step 3: Save to CSV
        csv_filename = f"{major}-{degree}-{title}.csv" 
        with open(csv_filename, "w", newline="", encoding="utf-8") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["Course Code", "Course Name", "Course Hours", "Requirement Group", "Number Required", "Enrolled"])
            csv_writer.writerows(courses)
        print(f"✅ Data written to {csv_filename}")
        csv_list += [f"{csv_filename}"]
    return csv_list


st.title("See Your Degree Track!")
st.write("Please input your major url to continue.")

url = st.text_input("Degree URL")
if url:

    degree = get_title(url)

    st.write(f"**Is this your degree?** {degree}")

    if st.button("Yes!"):
        major_degree = degree.split(",")
        major = major_degree[0].strip()
        major.replace(" ", "-")
        degree = major_degree[1].strip()
        
        csv_list = get_courses(url, major, degree)
        i = 0
        for file in csv_list:
            i += 1
            filepath = f"{file}"
            df = pd.read_csv(filepath)

# st.write("### Data Preview")
# st.dataframe(df)

            reqs_df = pd.read_csv(filepath)

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
                edited_df.to_csv(f"completed_{filepath}", index=False)
                st.success("Changes saved successfully!")
                
                personalised_df = pd.read_csv(f"completed_{filepath}")


                num_required = 0
                num_required_taken = 0
                req_groups = {} # req_group : num required, satisfied
                for row in personalised_df.itertuples():
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


                # Sample array data


                st.title("Percent of degree completed:")

                fig, ax = plt.subplots()
                colors = ["#A52A2A", "#660000"]  # Light red, blue, green, and orange

                ax.pie(all_req, labels=labels, colors=colors,autopct="%1.1f%%", startangle=90)
                ax.axis("equal")  # Equal aspect ratio ensures pie is drawn as a circle.

                st.pyplot(fig)



