import requests
from bs4 import BeautifulSoup

    
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


    # return the extracted title
    return (main_title)

# Pass the URL as an argument
get_title("https://catalog.northeastern.edu/undergraduate/computer-information-science/computer-science/bscs/#ARIN")
