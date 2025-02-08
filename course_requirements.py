def get_courses(major, degree):
    import requests
    from bs4 import BeautifulSoup
    import csv

    # Step 1: Fetch the catalog page
    url = f"https://catalog.northeastern.edu/undergraduate/computer-information-science/{major}/{degree}/#programrequirementstext"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    # soup = BeautifulSoup(''.join(response.content), "html.parser")
    h3s = soup.find_all("h3")
    arr = soup.prettify().split('<h3>')
    # Step 2: Find all tbody elements

    # Find all tables with the class "sc_courselist"
    tables = soup.find_all("table", class_="sc_courselist")

    all_h3_elements = []
    num = 0
    for table in tables:
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
        h3_elements = [sibling for sibling in preceding_siblings if sibling.name == "h3"]
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
                is_optional = "Complete" in comment_span.text
            # Skip section headers
            if "areaheader" in row.get("class", []):
                continue

            # Extract course information
            td_elements = row.find_all("td")
            if len(td_elements) >= 3:
                course_code = td_elements[0].text.strip()
                if "and" in course_code:
                    course_code = course_code.replace('\n', '')
                    course_code = ' '.join(course_code.split())
                course_name = td_elements[1].text.strip()
                if "and" in course_name:
                    course_name = course_name.replace('\n', '')
                    course_name = ' '.join(course_name.split())
                course_hours = td_elements[2].text.strip()

                courses.append([course_code, course_name, course_hours, current_group, is_optional])
        title = "Core"
        if all_h3_elements:
            title = all_h3_elements[-1].text
        # Step 3: Save to CSV
        csv_filename = f"{major}-{degree}-{title}-{num}.csv"
        with open(csv_filename, "w", newline="", encoding="utf-8") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["Course Code", "Course Name", "Course Hours", "Requirement Group", "Is Optional"])
            csv_writer.writerows(courses)
        num+=1
        print(f"✅ Data written to {csv_filename}")

    # # Print the text content of each h3 element
    # for h3 in all_h3_elements and part in arr:
    #     print(h3.text.strip())
        
    # for part in arr:
    #     # print(part)
    #     soup_test = (BeautifulSoup(part, "html.parser"))
    #     # print(soup_test.find('h3 tbody'))
    #     tbody_elements = soup_test.find_all("tbody")
    #     # print(tbody_elements)

    #     # Storage for courses
    #     courses = []  # (course_code, course_name, course_hours, requirement_group, is_optional)

    #     current_group = "General Requirements"  # Default group
    #     is_optional = False

    #     for tbody in tbody_elements:
    #         rows = tbody.find_all("tr")

    #         for row in rows:
    #             # Check if row contains a requirement group header
    #             # comment_td = row.find("td", colspan="2")
    #             # print(f"comment: {comment_td}")
    #             # if comment_td:
    #             requirement_group = row.find("span", class_="courselistcomment areaheader")

    #             if requirement_group:
    #                 current_group = requirement_group.text.strip()
    #             comment_span = row.find("span", class_="courselistcomment")
    #             if comment_span:
    #                 is_optional = "Complete" in comment_span.text
    #             # Skip section headers
    #             if "areaheader" in row.get("class", []):
    #                 continue

    #             # Extract course information
    #             td_elements = row.find_all("td")
    #             if len(td_elements) >= 3:
    #                 course_code = td_elements[0].text.strip()
    #                 if "and" in course_code:
    #                     course_code = course_code.replace('\n', '')
    #                     course_code = ' '.join(course_code.split())
    #                 course_name = td_elements[1].text.strip()
    #                 if "and" in course_name:
    #                     course_name = course_name.replace('\n', '')
    #                     course_name = ' '.join(course_name.split())
    #                 course_hours = td_elements[2].text.strip()

    #                 courses.append([course_code, course_name, course_hours, current_group, is_optional])

    #     # Step 3: Save to CSV
    #     csv_filename = "northeastern_courses.csv"
    #     with open(csv_filename, "w", newline="", encoding="utf-8") as csv_file:
    #         csv_writer = csv.writer(csv_file)
    #         csv_writer.writerow(["Course Code", "Course Name", "Course Hours", "Requirement Group", "Is Optional"])
    #         csv_writer.writerows(courses)

    #     print(f"✅ Data written to {csv_filename}")

get_courses('computer-science', 'bacs')

