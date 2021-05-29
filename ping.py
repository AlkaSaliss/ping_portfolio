import urllib.request
tmp = urllib.request.urlopen("https://alkai.herokuapp.com", timeout=60)
tmp = urllib.request.urlopen("https://alkai.netlify.app", timeout=60)


print(tmp.readlines())
