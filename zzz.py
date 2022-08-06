#!/data/data/com.termux/files/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from pprint import pprint

import requests
from rich import print, print_json

PROXIES = {
    "http": "socks5h://127.0.0.1:9050",
    "https": "socks5h://127.0.0.1:9050"
}

headers = {
    "Accept": "*/*",
    "Cookie": "p=mPbapIVCWkIPz5Pw; S=ar7cN5HQykuyTdkNdUZwng; Dark=true",
    "Connection": "keep-alive",
    "User-Agent":
    "Mozilla/5.0 (X11; Ubuntu; Linux aarch64; rv:75.0) Gecko/20100101 Firefox/75.0",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3"
}

payload = ""

url = "https://nvspc.biz/api/dummy/getShowcase?c=4H5U2pnf2kOy7-fO-5Pnbw"

r = requests.request("POST", url, data=payload, headers=headers)

#r.text[9:13]
str_json = json.dumps(r.json(), indent=2)  # json
data = json.loads(str_json)  # python

# город
citi = data['data']['Cities'][0]['N']
print(citi)
for item in data['data']['LN']:
    print(item['UID'], item['Name'])
