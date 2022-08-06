#!/data/data/com.termux/files/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
from rich import print

reqUrl = "https://nvspc.biz/api/dummy/getShowcase?c=4H5U2pnf2kOy7-fO-5Pnbw"

# Кореновск витрина эйфоретики
r = f'{reqUrl}&u=1&LNT=2&mic=0&mac=0&miw=0&maw=0&sortby=0&pad=0&count=25'

headersList = {
    "Accept": "*/*",
    "Cookie": "p=mPbapIVCWkIPz5Pw; S=ar7cN5HQykuyTdkNdUZwng; Dark=true",
    "Connection": "keep-alive",
    "User-Agent":
    "Mozilla/5.0 (X11; Ubuntu; Linux aarch64; rv:75.0) Gecko/20100101 Firefox/75.0",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3"
}

payload = ""

response = requests.request("POST", reqUrl, data=payload, headers=headersList)

pretty = json.dumps(response.json(), indent=2)

#  json.dumps(response.json(), indent=2)

with open('result.json', mode='w') as res:
    res.write(pretty)

#  print(response.text)
