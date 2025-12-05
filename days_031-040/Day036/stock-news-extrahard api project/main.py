import requests
from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = "NI9XON4TJHQWCKL4"
NEWS_API_KEY = "cc4b45ff4f99428aa58e856dcbfbf468"
params={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":API_KEY
}
account_sid = "ACac482b38ce7c103c7cc8239861de5dd3"
auth_token ="4aef65f9f492da6470400f149a2dd9e6"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get("https://www.alphavantage.co/query",params=params)
response.raise_for_status()
data = response.json()
print(data)
daily_data =data["Time Series (Daily)"]
list_daily_data = [value for value in daily_data.values()]
yesterdays_close = float(list_daily_data[0]["4. close"])
day_before_close = float(list_daily_data[1]["4. close"])

def percent_diff(yes,day_bef):
    diff = abs(yes - day_bef)
    return diff/day_bef * 100

up_or_down = None
if yesterdays_close > day_before_close:
    up_or_down = "🔺"
else :
    up_or_down = "🔻"


percen_change = round(percent_diff(yesterdays_close,day_before_close))
print(percen_change)

# Init

if percen_change > 1  :
    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

    # /v2/top-headlines
    params = {
        "apikey": NEWS_API_KEY,
        "q": COMPANY_NAME

    }
    response = requests.get("https://newsapi.org/v2/everything", params=params)
    data1 = response.json()
    articles_list = data1["articles"]
    selected_article_list = articles_list[:3]
    formatted_list = [f"{STOCK}: {up_or_down}{percen_change}%\nHeadline:{article['title']}\nBrief:{article['description']} " for article in
                      selected_article_list]
    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    client = Client(account_sid, auth_token)
    for article in formatted_list:
        message = client.messages.create(
            body= f"{article}",
            from_="+19789254737",
            to="+919645867995",
        )
        print(message.status)



## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

