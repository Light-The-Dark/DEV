import datetime
import sys
sys.stdout.reconfigure(encoding='utf-8')
import requests

# Parameters for Neve Yaakov, Jerusalem
PARAMETERS = {
    "lat": 31.837801,
    "lng": 35.240406,
    "tzid": "Israel",
    "formatted": 1,
}

# Gets the current day's sunset and returns it as datetime object
def get_sun_times():
    sunrise_sunset = requests.get("https://api.sunrise-sunset.org/json", params=PARAMETERS)
    sunrise_sunset.raise_for_status()
    sunset =  sunrise_sunset.json()
    sunset = sunset["results"]["sunset"]
    sunset = sunset[:5].replace(":", " ")
    sunset_hour, sunset_minute = map(int, sunset.split())
    return datetime.datetime.now().replace(hour=sunset_hour, minute=sunset_minute)

def mincha_erev(shkia_time):
    mincha_erev_time = shkia_time - datetime.timedelta(minutes=30)
    print(f"מנחה ערב שבת: {mincha_erev_time.strftime('%H:%M')}")

def avot_ubanim(shkia_time):
    avot_ubanim_time = shkia_time - datetime.timedelta(hours=1, minutes=45)
    print(f"אבות ובנים: {avot_ubanim_time.strftime('%H:%M')}")

def mincha_shabbat(shkia_time):
    mincha_shabbat_time = shkia_time - datetime.timedelta(hours=1)
    print(f"מנחה שבת: {mincha_shabbat_time.strftime('%H:%M')}")

def aravit_motzash(shkia_time):
    aravit_motzash_time = shkia_time + datetime.timedelta(minutes=37)
    print(f"ערבית מוצאי שבת: {aravit_motzash_time.strftime('%H:%M')}")





# Call the functions
shkia_time = get_sun_times()
mincha_erev(shkia_time)
avot_ubanim(shkia_time)
mincha_shabbat(shkia_time)
aravit_motzash(shkia_time)

input("Press Enter to exit...")

