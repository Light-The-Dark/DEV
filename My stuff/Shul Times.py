import datetime
import sys
sys.stdout.reconfigure(encoding='utf-8')

    
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
    aravit_motzash_time = shkia_time + datetime.timedelta(minutes=30)
    print(f"ערבית מוצאי שבת: {aravit_motzash_time.strftime('%H:%M')}")

shkia_h, shkiah_m = map(int, input("נא לכתוב זמן שקיעה אם רווח בין השעה לדקות: ").split())

# Create a datetime object for sunset time
shkia_time = datetime.datetime.now().replace(hour=shkia_h, minute=shkiah_m)

# Call the functions
mincha_erev(shkia_time)
avot_ubanim(shkia_time)
mincha_shabbat(shkia_time)
aravit_motzash(shkia_time)

input("Press Enter to exit...")

