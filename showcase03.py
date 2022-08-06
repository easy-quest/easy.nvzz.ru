#!/data/data/com.termux/files/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

reqUrl = "https://nvzzz.ru/api/FB62rUxbq06F6l3QlvjxKQ/getShowcase"

headersList = {
    "Accept": "*/*",
    "User-Agent": "Thunder Client (https://www.thunderclient.com)"
}

payload = ""

response = requests.request("POST", reqUrl, data=payload, headers=headersList)

print(response.text)
