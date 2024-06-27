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

with open("CI stuff/bank_info.json") as file:
    bank_values = file.read()

with open("CI stuff/charges_values.json", encoding="utf-8") as file:
    charges_values = file.read()

# NOTE terminal uid is hardcoded currently in data file
with open("CI stuff/token.json", encoding="utf-8") as file:
    token = file.read()

with open("CI stuff/api.txt") as file:
    api = file.readline()

with open("CI stuff/secret_key.txt") as file:
    secret = file.readline()



headers = {
  'Content-Type': 'application/json',
  'Authorization': f'{{"api_key":"{api}","secret_key":"{secret}"}}'
}

####################################################################################
# Handle responses, both to push changes and to request data
####################################################################################

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

def request_data(url, data=None):
    try:
        response = requests.get(url, headers=headers, data=data)
        response.raise_for_status()  
        print(response.text)
        return response.json()
    except requests.exceptions.HTTPError as e:
        print('HTTP Error:', e.response.status_code, e.response.reason)
    except requests.exceptions.RequestException as e:
        print('Request Exception:', e)


####################################################################################
# Adding/manipluating customers functions
####################################################################################

def add_customer(info):
    url = "https://restapidev.payplus.co.il/api/v1.0/Customers/Add"
    request_change(url, data=info)

def update_customer(uid, values):
    url = "https://restapidev.payplus.co.il/api/v1.0/Customers/Update/" + uid
    request_change(url, data=values)

def view_customer(email=None, vat_number=None, user_id=None):
    # Base URL
    base_url = "https://restapidev.payplus.co.il/api/v1.0/Customers/View?"

    # Initialize an empty list to collect parameters
    params = []

    # Add email if provided
    if email:
        params.append(f"email={email}")

    # Add vat_number if provided (and not None)
    if vat_number is not None:
        params.append(f"vat_number={vat_number}")

    # Add user_id if provided
    if user_id:
        params.append(f"user_id={user_id}")

    # Join all parameters with "&" and concatenate to the base URL
    url = base_url + "&".join(params)
    data = request_data(url)


    customer_uids = [customer['customer_uid'] for customer in data['customers']]
    try:
        return str(customer_uids[0])
    except:
        print("No customer found")
    
def remove_customer(uid):
    url = f"https://restapidev.payplus.co.il/api/v1.0/Customers/Remove/{uid}"
    request_change(url)




# add_customer(values)
uid = view_customer(email="aharon@example.com")
# update_customer(uid, values)
# view_customer()
# remove_customer(uid)



####################################################################################
# Bank functions
####################################################################################
# This replaces the blank uid in "bank_values" with a real uid
bank_values = bank_values.replace("{uid}", uid)


# NOTE!!!!! User ID needs to be in data, not in the url
def add_bank(bank_info):
    url = "https://restapidev.payplus.co.il/api/v1.0/Banks/CreateCustomerBankAccount"
    request_change(url, data=bank_info)

def update_bank_info(user_id):
    url = "https://restapidev.payplus.co.il/api/v1.0/Banks/UpdateCustomerBankAccount/" + user_id
    request_change(url, data=bank_values)

def view_bank_details(user_id):
    url = "https://restapidev.payplus.co.il/api/v1.0/Banks/CustomerBankAccounts/" + user_id
    data = request_data(url)
    try:
        return data["data"][0]["uid"]
    except:
        print("No bank details available")

# NOTE: user_id here refers to the special id of the bank not the original user id
def remove_bank_account(user_id):
    url = "https://restapidev.payplus.co.il/api/v1.0/Banks/RemoveCustomerBankAccount/" + user_id
    request_change(url)


# add_bank(bank_values)
# update_bank_info(uid)
# bank_uid = view_bank_details(uid)
# remove_bank_account(bank_uid)

####################################################################################
# Tokens == CC info
####################################################################################
# NOTE: Need to change token data per user. Required info: terminal uid, customer uid, cc info
token = token.replace("{uid}", uid)
token_parse = json.loads(token)
terminal_uid = token_parse["terminal_uid"]

data2 = f"""
    {{
    "terminal_uid": {terminal_uid},
    "customer_uid": "415314fd-88ed-4e0a-b35b-3d9ba68092060218"
    }}
    """

def add_cc():
    url = "https://restapidev.payplus.co.il/api/v1.0/Token/Add"
    request_change(url, data=token)

def remove_cc():
    url = "https://restapidev.payplus.co.il/api/v1.0/Token/Remove/" + card_id
    print(url)
    request_change(url)

def check_cc():
    url = "https://restapidev.payplus.co.il/api/v1.0/Token/Check/" + card_id
    request_data(url)

def view_cc():
    # Getting permission to decrpyt denied error
    url = "https://restapidev.payplus.co.il/api/v1.0/Token/View/" + card_id
    request_data(url)

def list():
    url = "https://restapidev.payplus.co.il/api/v1.0/Token/List/"
    # Needs customer uid and terminal uid
    print(url, data2)
    request_data(url, data2)
    
    
# add_cc()
# remove_cc()
# check_cc()
# view_cc()
# list()

####################################################################################
# Recurring transactions
####################################################################################
# NOTE: Requires products with categories first!!! Also tokens!!!
# NOTE: Terminal uid needs to be replaced with real number

charges_values = charges_values.replace("{uid}", uid)
# print(charges_values)

def add_recurring_payment():
    url = "https://restapidev.payplus.co.il/api/v1.0/RecurringPayments/Add"
    request_change(url, data=charges_values)

# add_recurring_payment()