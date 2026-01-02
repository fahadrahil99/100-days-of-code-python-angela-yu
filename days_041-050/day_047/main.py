from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()

my_gmail = os.environ["MY_GMAIL"]
password = os.environ["PASSWORD"]
my_yahoo = os.environ["MY_YAHOO"]
server  = os.environ["SERVER"]

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.6",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Brave\";v=\"143\", \"Chromium\";v=\"143\", \"Not A(Brand\";v=\"24\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",

}

practice_url = "https://www.amazon.com/Kafka-Shore-Haruki-Murakami/dp/1400079276/ref=sr_1_1?sr=8-1"

response = requests.get(url=practice_url,headers=header)
data = response.text

# print(data)

soup = BeautifulSoup(data,"html.parser")
print(soup.prettify())
selector = soup.find("span",class_ = "a-price-whole").getText()
price = float(selector.replace(",", "").strip())

product_title = soup.find(id="productTitle").getText().strip()
title = "".join(product_title)
print(title)

message = f"{title} is on sale for {price}."
print(message)
if price < 1000 :
    msg = (
        f"From: {my_yahoo}\n"
        f"To: fahadrahil24@gmail.com\n"
        f"Subject: Amazon Price Alert!\n\n"
        "Your tracked item is now below your target price.\n\n"
        f"{message}\n\n"
        "https://appbrewery.github.io/instant_pot/"
    )

    with smtplib.SMTP_SSL(server, 465) as connection:
        connection.login(my_yahoo, password)
        connection.sendmail(
            from_addr=my_yahoo,
            to_addrs="fahadrahil24@gmail.com",
            msg=msg.encode("utf-8")
        )


