import pandas as pd
import matplotlib.pyplot as plt
import os
import tarfile
import urllib

STOCK_PATH = os.path.join("datasets", "stocks")
STOCK_URL = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=NBL&outputsize=full&datatype=csv&apikey=ZCB343AS7CKA7S67"


def fetch_stock_data(stock_url = STOCK_URL, stock_path = STOCK_PATH):
    os.makedirs(stock_path, exist_ok=True)
    csv_path = os.path.join(stock_path, "stocks.csv")
    urllib.request.urlretrieve(stock_url, csv_path)


def load_stock_data(stock_path = STOCK_PATH):
    print(stock_path)
    csv_path = os.path.join(stock_path, "stocks.csv")
    df = pd.read_csv(csv_path)
    # Convert timestamp column to DateTime and sort ascending by the timestamp
    df['timestamp'] = pd.to_datetime(df.timestamp)
    df.sort_values(by='timestamp', ascending=True)
    return df


stockData = load_stock_data()
stockData.head()

stockData.info()

stockData.hist(bins=50, figsize=(20, 15))
plt.show()

# Example Data Visualization Commands
#sns.scatterplot(x='close', y='volume', data=df)
#sns.pairplot(df)
#sns.distplot(df['volume'])
#df[['timestamp','close']].set_index('timestamp').plot()

#plt.show()


