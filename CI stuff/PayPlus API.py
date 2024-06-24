import requests
import json

# These are fake values for testing
values = """
{
"customer_name": "TEST",
"email": "aharon@example.com",
"paying_vat": true,
"vat_number": 123456789,
"customer_number": 145789,
"notes": "",
"phone": "0583205418",
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
"business_city": "Jerusalem",
"business_postal_code": "432765",
"business_country_iso": "IL"
}
"""

with open("CI stuff/api.txt") as file:
    api = file.readline()

with open("CI stuff/secret_key.txt") as file:
    secret = file.readline()


headers = {
  'Content-Type': 'application/json',
  'Authorization': f'{{"api_key":"{api}","secret_key":"{secret}"}}'
}


def request_change(url, data=None):
    try:
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()  
        print(response.text)
        return response.json()
    except requests.exceptions.HTTPError as e:
        print('HTTP Error:', e.response.status_code, e.response.reason)
    except requests.exceptions.RequestException as e:
        print('Request Exception:', e)

def request_data(url):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  
        print(response.text)
        return response.json()
    except requests.exceptions.HTTPError as e:
        print('HTTP Error:', e.response.status_code, e.response.reason)
    except requests.exceptions.RequestException as e:
        print('Request Exception:', e)


#################################################################################


def add_customer():
    url = "https://restapidev.payplus.co.il/api/v1.0/Customers/Add"
    request_change(url)

def update_customer(uid):
    url = "https://restapidev.payplus.co.il/api/v1.0/Customers/Update/" + uid
    request_change(url)

# 
def view_customer():
    # Parameters are: email, vat_number, uuid
    param = "email=aharon@example.com"
    url = "https://restapidev.payplus.co.il/api/v1.0/Customers/View?" + param
    data = request_data(url)
    customer_uids = [customer['customer_uid'] for customer in data['customers']]
    print(customer_uids)
    try:
        return str(customer_uids[0])
    except:
        print("No customer found")
    
def remove_customer(uid):
    url = f"https://restapidev.payplus.co.il/api/v1.0/Customers/Remove/{uid}"
    request_change(url)




# add_customer()
# uid = view_customer()
# update_customer()
# remove_customer(uid)
# response(request_url)