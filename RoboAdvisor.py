
import requests
import json

print("requesting stock market data...")


request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&apikey=demo"
response = requests.get(request_url)
# print(type(response)) #class 'requests.models.response
# print(response.status_code)
# print(response.text)

parsed_response = json.loads

breakpoint()

print("hello")

quit()
