import pandas
import datetime
import random
import smtplib

##################### Extra Hard Starting Project ######################

dummy_email = "j20620337@gmail.com"
password = "xqes yver yedc czll"

birthdays = pandas.read_csv(r"C:\Users\alazarix\Files\Day-31\birthdays.csv")


todays_date = datetime.date.today().month, datetime.date.today().day


dict = {(data_row["month"], data_row["day"]):data_row for (index, data_row) in birthdays.iterrows()}



if todays_date in dict:
    with open(rf"C:\Users\alazarix\Files\Day-31\letter_templates\letter_{random.randint(1,3)}.txt", "r") as letter:
        modified_letter = letter.read()
        modified_letter = modified_letter.replace("[NAME]", dict[todays_date]["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=dummy_email, password=password)
        connection.sendmail(from_addr=dummy_email, 
                            to_addrs=dict[todays_date]["email"], 
                            msg="Subject: Happy Birthday!\n\n" + modified_letter)

else:
    print("Not found")
