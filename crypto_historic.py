import requests
import pandas as pd
from datetime import datetime
from tqdm import tqdm

# Define the API endpoint
url = "https://api.binance.com/api/v3/klines"

# Ask user for input
symbol = input("Enter symbol: ")
interval = input("Enter interval: ")
start_str = input("Enter start time (YYYY-MM-DD): ")

# Convert start time to Unix timestamp
start_time = int(datetime.timestamp(datetime.strptime(start_str, "%Y-%m-%d"))) * 1000
end_time = int(datetime.timestamp(datetime.now())) * 1000

# Make the API request with progress bar
params = {"symbol": symbol, "interval": interval, "startTime": start_time, "endTime": end_time}
response = requests.get(url, params=params)
response.raise_for_status()

# Convert the response to a pandas DataFrame
df = pd.DataFrame(response.json(), columns=["Open time", "Open", "High", "Low", "Close", "Volume", "Close time", "Quote asset volume", "Number of trades", "Taker buy base asset volume", "Taker buy quote asset volume", "Ignore"])
df["Open time"] = pd.to_datetime(df["Open time"], unit="ms")
df.set_index("Open time", inplace=True)

# Drop unnecessary columns
df.drop(["Close time", "Quote asset volume", "Number of trades", "Taker buy base asset volume", "Taker buy quote asset volume", "Ignore"], axis=1, inplace=True)

# Convert the columns to numeric
df = df.apply(pd.to_numeric)

# Normalize the data
df = (df - df.mean()) / df.std()

# Split the data into training and validation sets
train_size = int(len(df) * 0.8)
train_data = df.iloc[:train_size]
val_data = df.iloc[train_size:]

# Convert the data to PyTorch tensors
import torch
train_tensor = torch.tensor(train_data.values)
val_tensor = torch.tensor(val_data.values)
