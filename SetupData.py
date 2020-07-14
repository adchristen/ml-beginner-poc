import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load Stock Daily (OHLCV) data
csv_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=NBL&outputsize=full&datatype=csv&apikey=ZCB343AS7CKA7S67'
df = pd.read_csv(csv_url)

# Convert timestamp column to DateTime and sort ascending by the timestamp
df['timestamp'] = pd.to_datetime(df.timestamp)
df.sort_values(by='timestamp', ascending=True)

# Example Data Visualization Commands
#sns.scatterplot(x='close', y='volume', data=df)
sns.pairplot(df)
#sns.distplot(df['volume'])
#df[['timestamp','close']].set_index('timestamp').plot()

plt.show()


