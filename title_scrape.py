import requests
from bs4 import BeautifulSoup

def get_title(url):
    # Send HTTP request
    response = requests.get(url)

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract the full title
    title = soup.title.string

    # Split the title at the comma to get "Computer Science" and "BSCS"
    title_parts = title.split(",")
    
    # Extract "Computer Science" and change "BSCS" to "BACS"
    main_title = title_parts[0].strip()  # "Computer Science"
    degree = title_parts[1].split()[0].strip()  # Extracts "BSCS" (or equivalent)
    

    # Concatenate and print the final result
    final_title = f"{main_title}, {degree}"
    print("Website Title:", final_title)

# Pass the URL as an argument
get_title("https://catalog.northeastern.edu/undergraduate/computer-information-science/computer-science/bscs/#ARIN")
