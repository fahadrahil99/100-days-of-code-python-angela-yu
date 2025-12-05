
from datetime import datetime
import requests

pixel_end_point = "https://pixe.la/v1/users"

TOKEN = "slkdfksdhfjsddsfdf"
USERNAME = "fahadrahil1999"
user_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

# response = requests.post(url=pixel_end_point,json=user_params)
# print(response.text)

graph_end_point = f"{pixel_end_point}/{USERNAME}/graphs"

header = {
    "X-USER-TOKEN" : TOKEN,
}

GRAPH_ID = "myhabitgraph1"
graph_config = {
    "id":GRAPH_ID,
     "name":"Coding time",
    "unit":"minutes",
    "type":"float",
    "color":"sora",
}
# response = requests.post(url=graph_end_point,json=graph_config,headers=header)

post_end_point = f"{graph_end_point}/{GRAPH_ID}"
today = datetime.now()
yesteday = datetime(year=2025,month=10,day=21)
today_formatted = today.strftime("%Y%m%d")

quantity = input("How many minutes did you spend coding today?")
post_config = {
    "date":today_formatted,
    "quantity":quantity,
}


response = requests.post(url=post_end_point,json=post_config,headers=header)
print(response.text)
update_endpoint = f"{pixel_end_point}/{USERNAME}/graphs/{GRAPH_ID}/{yesteday.strftime("%Y%m%d")}"
edited_data = {
    "quantity":"120",
}
# response = requests.delete(url=update_endpoint,headers=header)
# print(response.text)