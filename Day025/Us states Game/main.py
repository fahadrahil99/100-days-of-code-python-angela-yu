# with open("./weather_data.csv") as file:
#     data = file.readlines()

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#
# print(temperature)
#
# import pandas as pd
# data = pd.read_csv("weather_data.csv")
# # temp = data["temp"]
# # # temp_list = temp.to_list()
# # #
# # # no_of_elements = len(temp_list)
# # # sum_of_temp = sum(temp_list)
# # # avg = sum_of_temp/no_of_elements
# # # # print(avg)
# # print(temp.max())
#
# # print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# print(monday)
# monday_temp = monday.temp[0]
# m_f_f =monday_temp*1.8+32
# print(m_f_f)
import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250814.csv")
grey = data[data["Primary Fur Color"] == "Gray"]
no_gray = len(grey)
# print(no_gray)
black = data[data["Primary Fur Color"] == "Black"]
no_black = len(black)
cinnamon = data[data["Primary Fur Color"] == "Cinnamon"]
no_cinnamon = len(cinnamon)

count_dic = {"Fur Color": ["Gray","Black","Cinnamon"],
             "Count": [no_gray,no_black,no_cinnamon],

             }

Final_count_csv = pd.DataFrame(count_dic)
Final_count_csv.to_csv("./Count.csv")
