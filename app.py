#!/data/data/com.termux/files/usr/bin/env python
# -*- coding: utf-8 -*-
from core.core import *
import requests
# Импорт модуля json Python
import json

cookies = {
    'S': 'ar7cN5HQykuyTdkNdUZwng',
    'Dark': 'true',
    'p': 'uYxK6VfvBeTsw3E2',
}

headers = {
    'User-Agent':
    'Mozilla/5.0 (X11; Ubuntu; Linux aarch64; rv:75.0) Gecko/20100101 Firefox/75.0',
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://nvspc.biz',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'S=ar7cN5HQykuyTdkNdUZwng; Dark=true; p=uYxK6VfvBeTsw3E2',
    'TE': 'Trailers',
}

data = {
    'c': '4H5U2pnf2kOy7-fO-5Pnbw',
    'u': '1',
    'LNT': '2',
    'sortby': '0',
    'pad': '0',
    'count': '25',
}

r = requests.post('https://nvspc.biz/api/dummy/getShowcase',
                  cookies=cookies,
                  headers=headers,
                  data=data)

# Вызовите функцию dumps() и передайте список Python
json_str = json.dumps(r.json())

print(type(r.json()))
#  print(response.text)
print(type(json_str))
