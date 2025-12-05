import requests
import datetime as dt


MY_LONG = 11.664425104411556
MY_LAT = 76.10052933112672

# response = requests.get("http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data = response.json()
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude,latitude)
parameters = {
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted":0,
}

response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data = response.json()
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)
time_now = dt.datetime.now()
hour_now = time_now.hour
