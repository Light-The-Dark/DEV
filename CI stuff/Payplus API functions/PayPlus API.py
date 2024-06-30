# TODO in PHP. Add customer info to DB and then add whatever relevant info ie. cc info
# TODO Make sure that all file formats are uniform. Right now, loading files as string and JSON.

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

with open("CI stuff/Payplus API functions/customer_info.json") as file:
    customer_info_local = json.load(file)

with open("CI stuff/Payplus API functions/bank_info.json") as file:
    bank_values = file.read()

with open("CI stuff/Payplus API functions/charges_values.json") as file:
    charges_values = file.read()

# NOTE terminal uid is hardcoded currently in data file
with open("CI stuff/Payplus API functions/cc_token.json", encoding="utf-8") as file:
    cc_token = file.read()

with open("CI stuff/Payplus API functions/api.txt") as file:
    api = file.readline()

with open("CI stuff/Payplus API functions/secret_key.txt") as file:
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
    # Views customer based on filters
    base_url = "https://restapidev.payplus.co.il/api/v1.0/Customers/View?"
    params = []

    if email:
        params.append(f"email={email}")

    if vat_number is not None:
        params.append(f"vat_number={vat_number}")

    if user_id:
        params.append(f"user_id={user_id}")

    url = base_url + "&".join(params)
    data = request_data(url)

    customer_uids = [customer['customer_uid'] for customer in data['customers']]

    # TODO return all info as filtered and then let user choose what to pick.
    # Currently this will return only the first customer as a str assuming that multiple customers have matching info in the query ie. same email.
    # Also, need to only return one variable instead of 2 but will leave for testing in the meantime
    try:
        return str(customer_uids[0]), data["customers"][0]
    except:
        print("No customer found")
    
def remove_customer(uid):
    url = f"https://restapidev.payplus.co.il/api/v1.0/Customers/Remove/{uid}"
    request_change(url)




# add_customer(values)
uid, customer_info_payplus = view_customer(email="aharon@example.com")
# update_customer(uid, values)
# view_customer()
# remove_customer(uid)

####################################################################################
# Bank functions
####################################################################################
### TEST AGAGIN TO MAKE SURE IT WORKS!!!!!

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
# NOTE: Need to change cc_token data per user/per card. Required info: terminal uid, customer uid, cc info

# Question. Do we save last 4 digits or whole card?
# Create a new json with cards attached to customer_uid ie {cards: {uid: "123". card: "456"} {uid: "321", card: "654"}}

cc_token = cc_token.replace("{uid}", uid)
cc_token_parse = json.loads(cc_token)
terminal_uid = cc_token_parse["terminal_uid"]

data2 = f"""
    {{
    "terminal_uid": {terminal_uid},
    "customer_uid": {uid}
    }}
    """

def add_cc():
    url = "https://restapidev.payplus.co.il/api/v1.0/Token/Add"
    data = request_change(url, data=cc_token)
    if data["results"]["status"] == "success":
        add_cc_info(data["data"]["card_uid"])
        # Returns just the cc_id
        return data["data"]["card_uid"]
    else:
        print(data["results"])

def add_cc_info(card_id):
    if "card_id" not in customer_info_local:
        print("If statement")
        customer_info_local["card_id"] = card_id
        with open("CI stuff/Payplus API functions/customer_info.json", "w") as file:
            json.dump(customer_info_local, file, indent=4)
    else:
        print("else statement")
        i = 1
        while f"card_id_{i}" in customer_info_local:
            i += 1
        customer_info_local[f"card_id_{i}"] = card_id
       
        with open("CI stuff/Payplus API functions/customer_info.json", "w") as file:
            json.dump(customer_info_local, file, indent=4)

def remove_cc(card_id):
    url = "https://restapidev.payplus.co.il/api/v1.0/Token/Remove/" + card_id
    print(url)
    request_change(url)

def check_cc(card_id):
    url = "https://restapidev.payplus.co.il/api/v1.0/Token/Check/" + card_id
    request_data(url)

# Getting permission to decrpyt denied error. Don't think it's relevant anyways since we only need last 4 digits
# def view_cc(card_id):
#     
#     url = "https://restapidev.payplus.co.il/api/v1.0/Token/View/" + card_id
#     request_data(url)

def list():
    url = "https://restapidev.payplus.co.il/api/v1.0/Token/List"
    # Needs customer uid and terminal uid
    # print(url, data2)
    request_change(url, data2)
    

# add_cc()
# remove_cc()
# check_cc(card_id)

# view_cc(card_id)
# list()
# add_cc_info()

####################################################################################
# Product Categories
####################################################################################
# NOTE: I didn't save the product categories local since I'm just trying to get the recurring payment to work

product_category_values = """
{
    "name": "Appliances",
    "valid": true
}
"""

def create_product():
    url = "https://restapidev.payplus.co.il/api/v1.0/Categories/Add"
    request_change(url, data=product_category_values)

def view_product():
    url = "https://restapidev.payplus.co.il/api/v1.0/Categories/View/?" + "5d6d68a6-b3ae-4c48-bae4-0611220e7768"
    request_data(url)

# create_product()
# view_product()

####################################################################################
# Products
####################################################################################
# NOTE: Same not as above. Hard coding category id temporarily

product_values = """
{
  "category_uid": "5d6d68a6-b3ae-4c48-bae4-0611220e7768",
  "name": "TV",
  "price": 1500.50,
  "currency_code": "ILS",
  "vat_type": 0
}
"""


def add_product():
    # Requires category id, name, price, currency code (ie USD), vat type 0-'vat included' OR 1-'vat not included' OR 2- 'exempt vat'
    url = "https://restapidev.payplus.co.il/api/v1.0/Products/Add"
    request_change(url, data=product_values)

def view_product():
    url = "https://restapidev.payplus.co.il/api/v1.0/Products/View/" + "?uid/2694911e-9d22-4a33-b720-00c048c1b006"
    request_data(url)

# add_product()
# view_product()

####################################################################################
# Recurring transactions
####################################################################################
# NOTE: Need to save recurring payment id, deleting any hard coded id even though it makes no dif since its all sandbox

charges_values = charges_values.replace("{uid}", uid)
recurring_payment_id = ""

terminal_uid2 = """
{
    "terminal_uid": "{uid}"
}
"""
terminal_uid2 = terminal_uid2.replace("{uid}", terminal_uid)


def add_recurring_payment():
    url = "https://restapidev.payplus.co.il/api/v1.0/RecurringPayments/Add"
    request_change(url, data=charges_values)

def remove_recurring_payment():
    url = "https://restapidev.payplus.co.il/api/v1.0/RecurringPayments/DeleteRecurring/" + recurring_payment_id
    request_change(url, data=terminal_uid2)


# add_recurring_payment()
# remove_recurring_payment()
