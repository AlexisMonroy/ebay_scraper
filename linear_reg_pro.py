import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Step 1: Collect and prepare your data
# Let's assume you have data on the amount sold, time period, and price of an item in three separate lists
amount_sold = [100, 200, 200, 100, 150]
time_period = [1, 2, 3, 4, 5]
price = [10, 5, 7, 10, 12]

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