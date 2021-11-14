# Stock Trading News Alert

it's my project capstone for sending an Alert using Twilio, News and Stock API to detect if the price of a stock increased or decreased to 5% range, it will send a message


## Setup

Environment Variables

`STOCK_API_KEY` Get from https://www.alphavantage.co/

`NEWS_API_KEY` Get from https://newsapi.org/

`TWILIO_API_KEY`, `TWILIO_AUTH_TOKEN`, `TWILIO_ACCOUNT_SID`, `TO_NUMBER`, `FROM_NUMBER` Get from https://www.twilio.com/console/gate


## Scripts to run
```
export STOCK_API_KEY=YOUR_STOCK_API_KEY; export NEWS_API_KEY=YOUR_NEWS_API_KEY; export TWILIO_API_KEY=YOUR_TWILIO_API_KEY; export TWILIO_AUTH_TOKEN=YOUR_TWILIO_AUTH_TOKEN; export TWILIO_ACCOUNT
_SID=YOUR_TWILIO_ACCOUNT_SID; export TO_NUMBER=YOUR_TO_NUMBER; export FROM_NUMBER=YOUR_FROM_NUMBER; python3 main.py
```

## Preview
![Stock Market Alert](img.jpeg)