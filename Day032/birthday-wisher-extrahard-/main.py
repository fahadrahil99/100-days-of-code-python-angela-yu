

import pandas as pd
import smtplib
import random
import datetime as dt

my_gmail = "rahilnkfahad@gmail.com"
password = "qkhemukwjnbfmzpe"

now = dt.datetime.now()
b_data = pd.read_csv("birthdays.csv")
today = now.today().day
month = now.today().month


selected_rows = b_data[b_data.month == month]
todays_b_day = selected_rows[selected_rows.day == today]

with open("letter_templates/letter_1.txt") as file1:
    letter_1 = file1.read()
with open("letter_templates/letter_2.txt") as file2:
    letter_2 = file2.read()
with open("letter_templates/letter_3.txt") as file3:
    letter_3 = file3.read()
letters_list = [letter_1,letter_2,letter_3]
for index,row in todays_b_day.iterrows():
    selected_letter = random.choice(letters_list)
    edited_letter = selected_letter.replace("[NAME]",row["name"])
    with smtplib.SMTP("smtp.gmail.com",port = 587) as connection:
        connection.starttls()
        connection.login(user=my_gmail,password=password)
        connection.sendmail(from_addr=my_gmail,to_addrs=row["email"],msg=f"subject:Happy Birthday!\n\n"
        f"{edited_letter}")








