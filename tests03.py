#!/data/data/com.termux/files/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

PROXIES = {
    "http": "socks5h://127.0.0.1:9050",
    "https": "socks5h://127.0.0.1:9050",
}

HEADERS = {
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
    'application/signed-exchange;v=b3;q=0.9',
    'User-Agent':
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 '
    'Safari/537.36 '
}

response = requests.head(url,
                         timeout=20,
                         proxies=PROXIES,
                         allow_redirects=False)
