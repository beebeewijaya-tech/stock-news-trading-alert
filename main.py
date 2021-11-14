import time
import os

import requests
from twilio.rest import Client

STOCK = "TSLA"
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
TIME_SERIES = "TIME_SERIES_DAILY"

COMPANY_NAME = "Tesla Inc"
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


TWILIO_API_KEY = os.environ.get("TWILIO_API_KEY")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")

message_format = """
    [STOCK_NAME]: 🔺[PERCENTAGE].
    Headline: [TITLE]. 
    Brief: [DESCRIPTION].
"""


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price.
stock_params = {
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
    "function": TIME_SERIES
}
stock_res = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_res.raise_for_status()

stock_json = stock_res.json()
stock_daily = stock_json["Time Series (Daily)"]
stock_daily_dict = {index: value for (index, (key, value)) in enumerate(stock_daily.items())}

stock_yesterday = stock_daily_dict[0]
stock_two_days_ago = stock_daily_dict[1]

difference_price = float(stock_yesterday["4. close"]) - float(stock_two_days_ago["4. close"])
percentage = difference_price / float(stock_two_days_ago["4. close"]) * 100


## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
#HINT 1: Think about using the Python Slice Operator
if percentage < 5 or percentage >= 5:
    news_params = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY
    }
    news_res = requests.get("https://newsapi.org/v2/everything", news_params)
    news_res.raise_for_status()

    news_json = news_res.json()
    news_sliced = news_json["articles"][:3]

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    # Send a separate message with each article's title and description to your phone number.
    # HINT 1: Consider using a List Comprehension.
    for news in news_sliced:
        title = news["title"]
        description = news["description"]

        percentage_message = ""

        if percentage > 0:
            percentage_message = f"🔺{percentage}%"
        else:
            percentage_message = f"🔻{percentage}%"

        message_manipulate = message_format\
                                .replace("[STOCK_NAME]", STOCK)\
                                .replace("[TITLE]", title)\
                                .replace("[DESCRIPTION]", description)\
                                .replace("[PERCENTAGE]", percentage_message)


        messages = client.messages\
            .create(
                to = os.environ.get("TO_NUMBER"),
                from_ = os.environ.get("FROM_NUMBER"),
                body = message_manipulate
            )


        print(messages.status)
        time.sleep(2)

