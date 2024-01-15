import requests
import datetime
import time
import smtplib

DUMMY_EMAIL = "j20620337@gmail.com"
PASSWORD = "xqes yver yedc czll"
LATITTUDE = 31.837801
LONGITUDE = 35.240406
PARAMETERS = {
    "lat": 31.837801,
    "lng": 35.240406,
    "tzid": "Israel",
    "formatted": 0,
}

# Gets the time of sunrise and sunset for Jerusalem, Israel (configured for Neve Yaakov times)
def get_sun_times():
    sunrise_sunset = requests.get("https://api.sunrise-sunset.org/json", params=PARAMETERS)
    sunrise_sunset.raise_for_status()
    sunrise_sunset = sunrise_sunset.json()

    sunrise = sunrise_sunset["results"]["sunrise"].split("T")
    sunset = sunrise_sunset["results"]["sunset"].split("T")
    return int(sunrise[1][:2]), int(sunset[1][:2])


# Checks the position of the ISS and if close to current position, prints current location, sends email only if close by and visible
def check_position():
    iss_api = requests.get("http://api.open-notify.org/iss-now.json")
    longitude = float(iss_api.json()["iss_position"]["longitude"])
    latitude = float(iss_api.json()["iss_position"]["latitude"])

    print(f"Current ISS position latitude: {latitude}, longitude: {longitude}")
    if (latitude - 5) <= LATITTUDE <= (latitude + 5) and (longitude - 5) <= LONGITUDE <= (longitude + 5):
        print("close by")
        if current_hour > sunset_hour and current_hour < sunrise_hour:
            send_email()
            print("sending email")
            

# Sends email to look up into the sky
def send_email():

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=DUMMY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=DUMMY_EMAIL,
                            to_addrs="aharonlazari@gmail.com",
                            msg="Subject: ISS overhead\n\n" 
                            + "LOOK UP!!! Super cool!!!!")
    

while True:

    current_hour = datetime.datetime.today().hour
    sunrise_hour, sunset_hour = get_sun_times()
    check_position()

    time.sleep(5)