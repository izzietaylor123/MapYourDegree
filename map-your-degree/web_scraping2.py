import requests
from bs4 import BeautifulSoup 
import json

def get_courses(url, major, degree):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    tables = soup.find_all("table", class_="sc_courselist")
    all_h3_elements = []
    courses = []

    for table in tables:
        current_group = "Default"
        num_required = "All"
        
        preceding_siblings = []
        current_sibling = table.previous_sibling
        while current_sibling:
            if current_sibling.name:
                preceding_siblings.append(current_sibling)
            current_sibling = current_sibling.previous_sibling

        preceding_siblings.reverse()
        h3_elements = [sibling for sibling in preceding_siblings if (sibling.name == "h3" or sibling.name == "h2")]
        all_h3_elements.extend(h3_elements)
        rows = table.find_all("tr")

        for row in rows:
            requirement_group = row.find("span", class_="courselistcomment areaheader")
            if requirement_group:
                current_group = requirement_group.text.strip()
            comment_span = row.find("span", class_="courselistcomment")
            if comment_span and "Complete" in comment_span.text:
                index = comment_span.text.split(" ").index("Complete")
                num_required = comment_span.text.split(" ")[index + 1]
                if "Default" in current_group:
                    current_group = current_group + "1"

            if "areaheader" in row.get("class", []):
                continue

            td_elements = row.find_all("td")
            if len(td_elements) >= 3 or (len(td_elements) == 2 and "or" in td_elements[0].text):
                course_code = td_elements[0].text.strip()
                if "and" in course_code:
                    course_code = ' '.join(course_code.replace('\n', '').split())
                course_name = td_elements[1].text.strip()
                if "and" in course_name:
                    course_name = ' '.join(course_name.replace('\n', '').split())
                course_hours = td_elements[2].text.strip() if len(td_elements) > 2 else ""

                courses.append({
                    "Course Code": course_code,
                    "Course Name": course_name,
                    "Course Hours": course_hours,
                    "Requirement Group": current_group,
                    "Number Required": num_required,
                    "Enrolled": False
                })

    title = all_h3_elements[-1].text if all_h3_elements else "Core"
    json_filename = f"public/{major}-{degree}-{title}.json"


    with open(json_filename, "w", encoding="utf-8") as json_file:
        json.dump(courses, json_file, indent=4)
    
    print(f"✅ Data written to {json_filename}")

get_courses(
    'https://catalog.northeastern.edu/undergraduate/business/business-administration-law-bs/#programrequirementstext', 
    'Business_admin_and_law', 
    'BS'
)
