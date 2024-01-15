# import smtplib

# dummy_email = "j20620337@gmail.com"
# password = "xqes yver yedc czll"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=dummy_email, password=password)
#     connection.sendmail(from_addr=dummy_email, to_addrs="aharonlazari@gmail.com", msg="Test")


import datetime as dt

now = dt.datetime.now()
year = now.year
weekday = now.weekday()
print(year)
print(weekday)

date_I_want = dt.datetime(year=2023, month=12, day=27)
print(date_I_want)