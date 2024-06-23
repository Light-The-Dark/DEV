from urllib.request import Request, urlopen
import urllib
import json

# These are fake values for testing
values = """
{
"customer_name": "Moshe cohen",
"email": "moshe@example.com",
"paying_vat": true,
"vat_number": 123456789,
"customer_number": 145789,
"notes": "",
"phone": "039666666",
"contacts": [
    {
        "full_name": "Moshe cohen",
        "cell_phone": "",
        "contact_email": "",
        "contact_address": "Haim Weizman 58",
        "contact_city": "Jerusalem",
        "contact_postal_code": "789465",
        "contact_country_iso": "IL",
        "job_position": ""
    }
],
"business_address": "Haim Weizman 12",
"business_city": "Holon",
"business_postal_code": "432765",
"business_country_iso": "IL",
}"""


with open (r"CI stuff\api.txt", "r") as file:
    api = file.readline()
    api_keys = api.strip()
    print(api_keys)

headers = {
"Content-Type": "application/json",
"Authorization": api_keys
}

print(headers)


data = values.encode("utf-8")

def response(request):
    try:
        with urlopen(request) as response:
            response_body = response.read()
            print(response_body.decode("utf-8"))
    except urllib.error.HTTPError as e:
        print('HTTP Error:', e.code, e.reason)
    except urllib.error.URLError as e:
        print('URL Error:', e.reason)

def add_customer(data):
    return Request('https://private-anon-3bb9e7ceb2-payplus.apiary-mock.com/api/v1.0/Customers/Add', data=data, headers=headers)

def update_customer(data):
    return Request('https://private-anon-3bb9e7ceb2-payplus.apiary-mock.com/api/v1.0/Customers/Update/:{uid}', data=data, headers=headers)

def view_customer(data):
    return Request('https://private-anon-3bb9e7ceb2-payplus.apiary-mock.com/api/v1.0/Customers/View?uuid={uuid}&vat_number={vat_number}&email={email}&skip={skip}&take={take} ', headers=headers)

def remove_customer(data):
    return Request('https://private-anon-3bb9e7ceb2-payplus.apiary-mock.com/api/v1.0/Customers/Remove/:{customer_uid}', data=data, headers=headers)




request = remove_customer(data)
response(request)



