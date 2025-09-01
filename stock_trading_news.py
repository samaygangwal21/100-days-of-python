import os
import requests
from twilio.rest import Client

# ----------------- CONFIGURATION -----------------
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# Read sensitive keys from environment variables
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_FROM_NUMBER = os.getenv("TWILIO_FROM_NUMBER")
TWILIO_TO_NUMBER = os.getenv("TWILIO_TO_NUMBER")


# ----------------- FETCH STOCK DATA -----------------
def get_stock_change(symbol):
    params = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": symbol,
        "apikey": STOCK_API_KEY
    }
    response = requests.get(STOCK_ENDPOINT, params=params)
    response.raise_for_status()
    data = response.json()["Time Series (Daily)"]

    # Get the last two closing prices
    dates = sorted(data.keys(), reverse=True)
    latest_close = float(data[dates[0]]["4. close"])
    previous_close = float(data[dates[1]]["4. close"])

    percent_change = ((latest_close - previous_close) / previous_close) * 100
    return round(percent_change, 2)


# ----------------- FETCH NEWS -----------------
def get_news(company_name, limit=3):
    params = {
        "qInTitle": company_name,
        "apiKey": NEWS_API_KEY,
        "sortBy": "publishedAt",
        "language": "en",
        "pageSize": limit
    }
    response = requests.get(NEWS_ENDPOINT, params=params)
    response.raise_for_status()
    articles = response.json().get("articles", [])
    news_list = [f"{article['title']}: {article['description']}" for article in articles]
    return news_list


# ----------------- SEND SMS -----------------
def send_sms(messages):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    for msg in messages:
        client.messages.create(
            body=msg,
            from_=TWILIO_FROM_NUMBER,
            to=TWILIO_TO_NUMBER
        )


# ----------------- MAIN LOGIC -----------------
if __name__ == "__main__":
    try:
        change_percent = get_stock_change(STOCK_NAME)
        print(f"{STOCK_NAME} stock changed by {change_percent}%")

        if abs(change_percent) >= 5:  # Send news if change >= 5%
            news_items = get_news(COMPANY_NAME)
            formatted_messages = [f"{STOCK_NAME} Alert: {change_percent}%\n{news}" for news in news_items]
            send_sms(formatted_messages)
            print("News sent via SMS.")
        else:
            print("Stock change is less than 5%, no news sent.")

    except Exception as e:
        print(f"Error: {e}")
