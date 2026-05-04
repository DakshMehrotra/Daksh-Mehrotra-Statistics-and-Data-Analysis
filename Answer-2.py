import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA

from sklearn.metrics import mean_absolute_error, mean_squared_error

import warnings
warnings.filterwarnings('ignore')


# Load dataset
sales_df = pd.read_csv('/content/train.csv')

sales_df.head()


import pandas as pd

# Load dataset
sales_df = pd.read_csv('train.csv')

# Convert Order Date column to datetime
sales_df['Order Date'] = pd.to_datetime(
    sales_df['Order Date'],
    dayfirst=True
)

# Set as index
sales_df.set_index('Order Date', inplace=True)

# Sort by date
sales_df.sort_index(inplace=True)

# Display first rows
sales_df.head()


# Check missing values
print(sales_df.isnull().sum())

# Fill missing values
sales_df.fillna(method='ffill', inplace=True)


plt.figure(figsize=(14,6))

plt.plot(sales_df['Sales'])

plt.title('Daily Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')

plt.show()


decomposition = seasonal_decompose(
    sales_df['Sales'],
    model='additive',
    period=30
)

decomposition.plot()

plt.show()


result = adfuller(sales_df['Sales'])

print('ADF Statistic:', result[0])
print('p-value:', result[1])


sales_diff = sales_df['Sales'].diff().dropna()

# Plot differenced data
plt.figure(figsize=(12,5))

plt.plot(sales_diff)

plt.title('Differenced Sales Data')

plt.show()


train = sales_df['Sales'][:-30]
test = sales_df['Sales'][-30:]


# Build model
model = ARIMA(train, order=(5,1,2))

model_fit = model.fit()

print(model_fit.summary())


forecast = model_fit.forecast(steps=30)


plt.figure(figsize=(12,6))

plt.plot(test.index, test, label='Actual')
plt.plot(test.index, forecast, label='Forecast')

plt.title('Actual vs Forecast Sales')

plt.legend()

plt.show()


mae = mean_absolute_error(test, forecast)

rmse = np.sqrt(mean_squared_error(test, forecast))

print("MAE:", mae)
print("RMSE:", rmse)
