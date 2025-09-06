import os
import math
import requests
from twilio.rest import Client

from dotenv import load_dotenv
load_dotenv()

STOCK_NAME = os.getenv("STOCK_NAME")
COMPANY_NAME = os.getenv("COMPANY_NAME")

STOCK_ENDPOINT = os.getenv("STOCK_ENDPOINT")
NEWS_ENDPOINT = os.getenv("NEWS_ENDPOINT")

STOCK_API_KEY = os.getenv("STOCK_API")
NEWS_API_KEY = os.getenv("NEWS_API")

ACCOUNT_SID = os.getenv('ACCOUNT_SID')
AUTH_TOKEN = os.getenv('AUTH_TOKEN')

stock_params = {
  "function": "TIME_SERIES_DAILY",
  "symbol": STOCK_NAME,
  "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)

data = response.json()["Time Series (Daily)"]

data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterdays_closing_price = yesterday_data["4. close"]

day_before_yesterdays_data = data_list[1]
day_before_yesterdays_closing_price = day_before_yesterdays_data["4. close"]


# Price be high on other days and required is positive
difference_closing_price = float(yesterdays_closing_price) - float(day_before_yesterdays_closing_price)
final_difference = math.floor(abs(difference_closing_price))

diff_percent = (final_difference / float(yesterdays_closing_price) * 100)

if diff_percent < 5:
  news_params = {
    "q":COMPANY_NAME,
    "apiKey":NEWS_API_KEY
  }

  news_response = requests.get(NEWS_ENDPOINT, params=news_params)
  articles = news_response.json()["articles"]
  three_articles = articles[0:3]

  formatted_article = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

  client = Client(ACCOUNT_SID, AUTH_TOKEN)

  import time

  for i, article in enumerate(formatted_article):
      article = f"Part {i+1}:\n{article}"
      message = client.messages.create(
          body=article,
          from_=os.getenv("FROM_NUMBER"),
          to=os.getenv("TO_NUMBER"),
      )
      print(f"Message {i+1} sent: SID={message.sid}")
      time.sleep(2)  # wait before sending next

