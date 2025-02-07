# import requests
# from bs4 import BeautifulSoup
# import sqlite3

# # URL = "https://catalog.northeastern.edu/undergraduate/computer-information-science/computer-science/bacs/#programrequirementstext"
# # text = requests.get(URL).text
# # print(text)


# # Step 1: Fetch the page
# URL = "https://catalog.northeastern.edu/undergraduate/computer-information-science/computer-science/bacs/#programrequirementstext"
# headers = {"User-Agent": "Mozilla/5.0"}
# response = requests.get(URL, headers=headers)
# soup = BeautifulSoup(response.text, "html.parser")

# # Step 2: Find course tables
# cs_courses = []
# program_requirements_section = soup.find(tableclass ="sc_courselist")
# if program_requirements_section:
#     course_rows = program_requirements_section.find_all("tr")  # Look for rows inside tables
#     for row in course_rows:
#         cols = row.find_all("td")  # Find columns in each row
#         if len(cols) >= 2:  # Ensure there's enough data
#             title = cols[0].text.strip()  # Course title/code
#             credits = cols[-1].text.strip()  # Last column often has credit info
#             description = "N/A"  # Descriptions may not be in tables
#             cs_courses.append((title, description, credits))

# # Step 3: Store in SQLite
# conn = sqlite3.connect("nu_bacs_courses.db")
# cursor = conn.cursor()
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS cs_courses (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         title TEXT,
#         description TEXT,
#         credits TEXT
#     )
# """)
# cursor.executemany("INSERT INTO cs_courses (title, description, credits) VALUES (?, ?, ?)", cs_courses)
# conn.commit()
# conn.close()

# print(f"✅ Scraped and stored {len(cs_courses)} courses.")

import requests
from bs4 import BeautifulSoup

url = "https://catalog.northeastern.edu/undergraduate/computer-information-science/computer-science/bacs/#programrequirementstext"  # Replace with the actual URL
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find the parent div
parent_div = soup.find("div", id="programrequirementstextcontainer")

# Find all tables with the class 'sc_courselist' within the parent div
tables = parent_div.find_all("table", class_="sc_courselist")

# Iterate through the tables
for table in tables:
    # Process each table here
    print(table.text)
    print()
