from base64 import b64encode
import requests
import json
import re

def get_mpesa_auth_token():
    try:
        consumer_key = "DBKT6n6IXsxGt1vwueGB1pygGrlII1PX"
        consumer_secret =  "jGJA828Jt97lP9k0"

        #encode key:secret to base64
        key_secret = consumer_key+":"+consumer_secret
        bytes = key_secret.encode('ascii')
        b64_bytes = b64encode(bytes)
        b64_token = b64_bytes.decode('ascii')
        
        auth_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate"

        querystring = {"grant_type":"client_credentials"}
        payload = ""
        headers = {
            "Authorization": f"Basic {b64_token}"
        }

        # call mpesa auth endpoint
        response = requests.request("GET", auth_url, data=payload, headers=headers, params=querystring)
        if response.status_code == 200:
            token = json.loads(response.text).get('access_token')
            return token
        else:
            return ''
    except Exception as e:
        return e
        
def format_phone_no(phone):
    # remove special chars 
    phone = re.sub(r'[^0-9]', '', phone)

    # append correct country code
    if phone[0] == '0':
        phone = '254'+phone[1:]

    return phone