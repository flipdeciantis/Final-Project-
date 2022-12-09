#code to collect GDP and Retail Sales data
import requests
import json
from IPython.display import Image, display 
from app.alpha import API_KEY
from pandas import read_csv

def format_pct(my_number):
    """
    Formats a percentage number like 3.6555554 as percent, rounded to two decimal places.
    Param my_number (float) like 3.6555554
    Returns (str) like '3.66%'
    """
    return f"{my_number:.2f}%"


def display_feed(symbol="NFLX"):
    API_KEY = input("Please input your ALPHAVANTAGE API KEY: ")
    request_url = f"https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers={symbol}&apikey={API_KEY}"
    
    response = requests.get(request_url)

    data = json.loads(response.text)
    #print(type(data)) #> dict
    #print(data.keys())
    if "feed" not in data.keys():
        print(data)
        return None

API_KEY = input("Please input your ALPHAVANTAGE API KEY: ")

def fetch_GDP_data():
    """Fetches GDP data from the AlphaVantage API. Returns a list of dictionaries."""
    
    request_url = f"https://www.alphavantage.co/query?function=REAL_GDP&apikey={API_KEY}"

    response = requests.get(request_url)

    parsed_response = json.loads(response.text)
    
    return parsed_response["data"]

def fetch_RS_data():
    """Fetches GDP data from the AlphaVantage API. Returns a list of dictionaries."""
    
    request_url = f"https://www.alphavantage.co/query?function=RETAIL_SALES&apikey={API_KEY}"

    response = requests.get(request_url)

    parsed_response = json.loads(response.text)
    
    return parsed_response["data"]


if __name__ == "__main__":

    print("GDP REPORT...")

    data = fetch_GDP_data()

    print("-------------------------")
    print("LATEST GDP RATE:")
    print(f"{data[0]['value']}", "as of", data[0]["date"])

    print("Retail Sales REPORT...")

    data = fetch_RS_data()

    print("-------------------------")
    print("LATEST Retail Sales RATE:")
    print(f"{data[0]['value']}", "as of", data[0]["date"])