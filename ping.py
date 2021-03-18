import requests
tmp = requests.get("https://alkai.herokuapp.com", timeout=60)
print(tmp.text)
