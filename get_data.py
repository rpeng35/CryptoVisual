import config
import csv
from binance.client import Client

client = Client(config.API_KEY, config.API_SECRET)

# prices = client.get_all_tickers()

# for i in prices:
#     print(i)

candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)

csvfile = open('daily.csv', 'w', newline='')
candlestick_writer = csv.writer(csvfile, delimiter=',',)

# for candle in candles:
#     print(candle)

#     candlestick_writer.writerow(candle)


candles = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2019", "7 Feb, 2021")

for candle in candles:
    candle[0] = candle[0] / 1000
    candlestick_writer.writerow(candle)

csvfile.close