#!/data/data/com.termux/files/usr/bin/env python
# -*- coding: utf-8 -*-

# Витрина
from rich import print as rprint
# from rich import print_json
from rich.console import Console

console = Console()
import requests

PROXIES = {
    "http": "socks5h://127.0.0.1:9050",
    "https": "socks5h://127.0.0.1:9050",
}

url = "http://nvzzz.ru/api/FB62rUxbq06F6l3QlvjxKQ"

r = requests.post(f'{url}/getShowcase?c=4H5U2pnf2kOy7-fO-5Pnbw',
                  proxies=PROXIES)

# wjosn = print(rr.json())

# json_object = json.dumps(rr.content, indent=2)
# with open('витрина.json', 'w') as f:
# f.write(rr.json())

# with open('fil.json', 'wb') as file:
# file.write(str(rr.json()))

rprint(r.json())
