import requests

url = "https://nvspc.biz/api/u4H-5t3hM0eMprf6kowrpw/getShowcase"

#  querystring = {"c":""}

#  headers = {'user-agent': 'vscode-restclient'}

r = requests.post(url)
# response = requests.get(url)

# r.raise_for_status()  # raises exception when not a 2xx response
# if r.status_code != 204:
# r.text

print(r.text)
