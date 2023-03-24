import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Step 1: Collect and prepare your data
# Let's assume you have data on the amount sold, time period, and price of an item in three separate lists
amount_sold = [100, 150, 200, 250, 300]
time_period = [1, 2, 3, 4, 5]
price = [10, 12, 14, 16, 18]

# Combine the amount_sold and time_period lists into a single 2D array of predictor variables
X = np.column_stack((amount_sold, time_period))

# Convert the price list into a 1D array of response variables
y = np.array(price)

# Step 2: Split your data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Step 3: Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 4: Evaluate your model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print(f'Root Mean Squared Error: {rmse}')

# Create a line plot of the past prices and the predicted price
plt.plot(time_period, price, label='Past Prices')
new_data = np.array([[350, 6]]) # new data on amount sold and time period
predicted_price = model.predict(new_data)
plt.plot(6, predicted_price[0], 'ro', label='Predicted Price')
plt.xlabel('Time Period')
plt.ylabel('Price')
plt.legend()
plt.show()

print(predicted_price)

# Step 5: Use your model to make predictions
# Let's assume you have new data on the amount sold and time period of an item
new_data = np.array([[350, 6]]) # new data on amount sold and time period

# Use your model to make a prediction on the new data
predicted_price = model.predict(new_data)
print(predicted_price)

# Step 6: Save your model
import pickle
pickle.dump(model, open('model.pkl', 'wb'))

# Step 7: Load your model
model = pickle.load(open('model.pkl', 'rb'))

# Step 8: Use your model to make predictions
new_data = np.array([[350, 6]]) # new data on amount sold and time period
predicted_price = model.predict(new_data)
print(predicted_price)

# Path: ebay\price_v3.py
# Compare this snippet from ebay\price_v3.py:
# import requests
# from bs4 import BeautifulSoup
#
# # Set the base URL for eBay search results
# base_url = 'https://www.ebay.com/sch/i.html?_nkw='
#
# # Set the keyword you want to search for
# user_input = input('Enter a keyword to search for: ')
#
# # Set the keyword you want to search for
# keyword = user_input
# # Construct the full URL for the search results page
# url = base_url + keyword
#
# # Use requests to download the page content
# page = requests.get(url)
#
# # Parse the page content using BeautifulSoup
# soup = BeautifulSoup(page.content, 'html.parser')
#
# # Find all elements containing listing information
# listings = soup.find_all('li', class_='s-item')
#
# # Limit the number of listings to 10
# listings = listings[:10]
#
# # Loop through each listing and extract its sell price and URL
# for listing in listings:
#     # Find the element containing the sell price
#     price_element = listing.find('span', class_='s-item__price')
#
#     # Check if a price was found
#     if price_element:
#         # Extract and print the sell price
#         sell_price = price_element.text
#         print(f'Sell price: {sell_price}')
#
#     # Find the element containing the listing URL
#     url_element = listing.find('a', class_='s-item__link')
#
#     # Check if a URL was found
#     if url_element:
#         # Extract and print the listing URL
#         listing_url = url_element['href']
#         print(f'Listing URL: {listing_url}')

