# Retrieve Historical Price Data from Binance API for Torc
This project shows how to use the Binance API to retrieve historical price data for a given cryptocurrency and prepare the data for PyTorch.


### Installation
To run this project, you need to have Python 3 installed. You also need to install the required libraries by running the following command:

```sh
pip install -r requirements.txt
```


### To use this project, you need to provide the following inputs:

- symbol: The cryptocurrency symbol, e.g. BTCUSDT
- interval: The time interval for the data, e.g. 1h, 1d, 1w
- start time: The start time for the data, in the format YYYY-MM-DD

### You can run the project by running the following command:

```sh
python crypto_historic.py
```

This will prompt you to enter the required inputs and then retrieve the historical price data from the Binance API. The data is then normalized and split into training and validation sets, which are converted to PyTorch tensors for machine learning.
