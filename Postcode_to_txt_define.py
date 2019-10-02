# Import the necessaries
import requests
import json

# Define function to change API URL to json dictionary
def postcode_to_json(postcode, url):
    resp = requests.get(url+postcode)
    return resp.json()


# Define function to change API URL to text
def postcode_to_text(postcode, url):
    resp = requests.get(url+postcode)
    return resp.text

# Define function to get the status code of a URL
def postcode_status_request(postcode, url):
    resp = requests.get(url+postcode)
    return resp.status_code

def write_to_file(file, order_item):
    try:
        with open(file, 'a') as opened_file:
            opened_file.write(order_item + '\n')

        opened_file.close()
    except FileNotFoundError:
        print('File not Found')
