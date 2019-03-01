import requests
import json

print("requesting stock market data...")

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&apikey=demo"
response = requests.get(request_url)
# print(type(response)) #class 'requests.models.response
# print(response.status_code)
# print(response.text)

parsed_response = json.loads(response.text)

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

tsd = parsed_response["Time Series (Daily)"]
#I don't understand the error that I'm getting here

dates = list(tsd.keys())

latest_day = dates[0]
latest_close = tsd[latest_day]["4. close"]

high_prices = []
low_prices = []

for date in dates:
    high_price = tsd[date]["2. high"]
    low_prices = tsd[date]["3. low"]
    high_prices.append(float(high_price))
    high_prices.append(float(low_price))

recent_low = min(low_prices)


recent_high = max(high_prices)

print(f"Latest day: {last_refreshed}")
print(f"Latest close:{to_usd(float(latest_close))}")
print(f"Recent high: {to_usd(float(recent_high))}")
print(f"Recent low: {to_usd(float(recent_low))}")

#writing csv file into directory

#recommend why on own
#use values to create recommendations

# csv-mgmt/write_teams.py
#WRITE CSV FILE TO DATA BROWSER
# 
# import csv

#csv_file_path = "prices.csv" # a relative filepath

csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "monthly_sales.csv")

with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=["city", "name"])
    writer.writeheader() # uses fieldnames set above
    writer.writerow({"city": "New York", "name": "Yankees"})
    writer.writerow({"city": "New York", "name": "Mets"})
    writer.writerow({"city": "Boston", "name": "Red Sox"})
    writer.writerow({"city": "New Haven", "name": "Ravens"})