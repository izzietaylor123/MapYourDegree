import requests
from bs4 import BeautifulSoup 
import csv
def get_all_cip(url, school):
    url = f"{url}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    
    # Step 2: Find all tbody elements

    # Find all tables with the class "sc_courselist"
    tables = soup.find_all("table", class_="visible grid sc_majorciptable")
    print(tables)

    for table in tables:
        courses = []
        rows = table.find_all("tr")
        for row in rows:
            td_elements = row.find_all("td")
            if (len(td_elements) >= 3 or (len(td_elements) == 2 and "or" in td_elements[0].text)):
                academic_program = td_elements[0].text.strip()
                if "Academic Program" in academic_program:
                    academic_program = academic_program[16:].strip()
                major_transcript_title = td_elements[1].text.strip()
                if "Major Transcript Title" in major_transcript_title:
                    major_transcript_title = major_transcript_title[22:].strip()
                CIP = td_elements[2].text.strip()
                if "Major Cip Code" in CIP:
                    CIP = CIP[14:].strip()

                courses.append([academic_program, major_transcript_title, CIP])
        # Step 3: Save to CSV
        csv_filename = f"CIP-{school}.csv" 
        with open(csv_filename, "w", newline="", encoding="utf-8") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["Academic Program", "Major Transcript Title", "Major CIP Code"])
            csv_writer.writerows(courses)
        print(f"✅ Data written to {csv_filename}")
get_all_cip('https://catalog.northeastern.edu/general-information/major-cip-codes/', 'northeastern')