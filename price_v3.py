import requests
from bs4 import BeautifulSoup

# Set the base URL for eBay search results
base_url = 'https://www.ebay.com/sch/i.html?_nkw='

# Set the keyword you want to search for
user_input = input('Enter a keyword to search for: ')

# Set the keyword you want to search for
keyword = user_input
# Construct the full URL for the search results page
url = base_url + keyword

# Use requests to download the page content
page = requests.get(url)

# Parse the page content using BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

# Find all elements containing listing information
listings = soup.find_all('li', class_='s-item')

# Limit the number of listings to 10
listings = listings[:10]

# Loop through each listing and extract its sell price and URL
for listing in listings:
    # Find the element containing the sell price
    price_element = listing.find('span', class_='s-item__price')
    
    # Check if a price was found
    if price_element:
        # Extract and print the sell price
        sell_price = price_element.text
        print(f'Sell price: {sell_price}')
    
    # Find the element containing the listing URL
    url_element = listing.find('a', class_='s-item__link')
    
    # Check if a URL was found
    if url_element:
        # Extract and print the listing URL
        listing_url = url_element['href']
        print(f'Listing URL: {listing_url}')