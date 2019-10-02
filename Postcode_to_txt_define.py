import requests
import json

def postcode_to_json(postcode, url):
    resp = requests.get(url+postcode)
    return resp.json()

def postcode_to_text(postcode, url):
    resp = requests.get(url + postcode)
    return resp.text()

def postcode_status_request(postcode, url):
    resp = requests.get(url + postcode)
    return resp.status_code()
