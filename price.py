import requests
from bs4 import BeautifulSoup

# Set the base URL for eBay search results
base_url = 'https://www.ebay.com/sch/i.html?_nkw='

user_input = input('Enter a keyword to search for: ')

# Set the keyword you want to search for
keyword = user_input

# Construct the full URL for the search results page
url = base_url + keyword

# Use requests to download the page content
page = requests.get(url)

# Parse the page content using BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

# Find the element containing the total number of results
results_count = soup.find('h1', class_='srp-controls__count-heading').text

# Extract and print the total number of results
print(f'Total number of results: {results_count}')