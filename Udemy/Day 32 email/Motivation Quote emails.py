import datetime as dt
import random
import smtplib

DUMMY_EMAIL = 
PASSWORD = 

with open(r"C:\Users\alazarix\Files\Day-31\quotes.txt", mode="r") as quotes:
    random_quote = random.choice(quotes.readlines())

weekday_today = dt.datetime.now().weekday()

## Change the weekday_today to whatever day you want the thing to send out an email

if weekday_today == 3:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=DUMMY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=DUMMY_EMAIL,
                            to_addrs="aharonlazari@gmail.com",
                            msg="Subject: Random quote sent via Python script\n\n" 
                            + random_quote)
