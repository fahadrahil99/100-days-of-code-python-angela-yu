import requests
from twilio.rest import Client


account_sid = "ACac482b38ce7c103c7cc8239861de5dd3"
auth_token ="4aef65f9f492da6470400f149a2dd9e6"

MY_KEY ="e90c823485946776a88eb910fd5f1750"
MY_LAT = 11.664425104411556
MY_LONG = 76.10052933112672
l_lat = 51.5072
l_lon = -0.1276
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid":MY_KEY,
    "cnt":4,
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast",params=parameters)
response.raise_for_status()
data = response.json()
w_id_list =[]
will_rain = False
for x in range(4):
    weather = data["list"][x]["weather"][0]["id"]
    w_id_list.append(weather)
    if weather < 700 :
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Bring an umbrella",
        from_="+19789254737",
        to="+919645867995",
    )

    print(message.status)