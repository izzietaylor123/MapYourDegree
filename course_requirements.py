import pandas 

def get_courses(url, major, degree):
    import requests
    from bs4 import BeautifulSoup
    import csv

    # Step 1: Fetch the catalog page
    url = f"{url}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    
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

                courses.append([course_code, course_name, course_hours, current_group, num_required])
        title = "Core"
        if all_h3_elements:
            title = all_h3_elements[-1].text
        # Step 3: Save to CSV
        csv_filename = f"{major}-{degree}-{title}.csv" 
        with open(csv_filename, "w", newline="", encoding="utf-8") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["Course Code", "Course Name", "Course Hours", "Requirement Group", "Number Required"])
            csv_writer.writerows(courses)
        print(f"✅ Data written to {csv_filename}")


get_courses('https://catalog.northeastern.edu/undergraduate/computer-information-science/computer-science/bacs/#programrequirementstext', 'Computer_Science', 'BACS')
filepath = "/Users/izzietaylor/Documents/spring 2025/hackbeanpot/Computer_Science-BACS-Supporting Courses-1.csv"
df = pandas.read_csv(filepath)

print(df)