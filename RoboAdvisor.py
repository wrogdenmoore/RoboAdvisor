import requests
import json
import os 

print("requesting stock market data...")

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)


#api key on .env



symbol = "MSFT"
api_key = "demo"os.environment.get("ALPHAVANTAGE_API_KEY")
request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
#connect with API key
response = requests.get(request_url)
# print(type(response)) #class 'requests.models.response
# print(response.status_code)
# print(response.text)

print(json.dump)


parsed_response = json.loads(response.text)

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

tsd = parsed_response[("Time Series (Daily)")]
#I don't understand the error that I'm getting here

dates = list(tsd.keys())

latest_day = dates[0]
latest_close = tsd[latest_day]["4. close"]

high_prices = []
low_prices = []

for date in dates:
    high_price = tsd[date]["2. high"]
    low_price = tsd[date]["3. low"]
    high_prices.append(float(high_price))
    low_prices.append(float(low_price))

recent_low = min(low_prices)


recent_high = max(high_prices)


#print(recommendation)

#writing csv file into directory

#recommend why on own
#use values to create recommendations

# csv-mgmt/write_teams.py
#WRITE CSV FILE TO DATA BROWSER
# 
import csv

csv_file_path = "prices.csv"
#csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

#csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "monthly_sales.csv")

#not getting the csv filepath to appear--should be in directory

#with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
  
csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

with open(csv_file_path, "w") as csv_file:

    writer = csv.DictWriter(csv_file, fieldnames= csv_headers)
    writer.writeheader()
    for date in dates: {(
        daily_prices = tsd[date]
        writer.writerow({
            "timestamp": date,
            "open": daily_prices["1. open"],
            "high": daily_prices["2. high"],
            "low": daily_prices["3. low"],
            "close": daily_prices["4. close"],
            "volume": daily_prices["5. volume"],
        })


print("-----------------------")
print("CRUNCHING THE DATA...")
print("-----------------------")
print(f"Latest day: {last_refreshed}")
print("-----------------------")
print(f"Latest close:{to_usd(float(latest_close))}")
print("-----------------------")
print(f"Recent high: {to_usd(float(recent_high))}")
print("-----------------------")
print(f"Recent low: {to_usd(float(recent_low))}")
print("-----------------------")


# ... etc.        

 #   writer.writerow({"city": "New York", "name": "Yankees"})
   # writer.writeheader() # uses fieldnames set above
   # writer.writerow({"city": "New York", "name": "Yankees"})
   # writer.writerow({"city": "New York", "name": "Mets"})
   # writer.writerow({"city": "Boston", "name": "Red Sox"})
   # writer.writerow({"city": "New Haven", "name": "Ravens"})