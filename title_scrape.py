import requests
from bs4 import BeautifulSoup
import csv

def get_title(url):
    # URL to scrape
    url = "https://example.com"

    # Send HTTP request
    response = requests.get(url)

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract and print the title
    title = soup.title.string
    print("Website Title:", title)