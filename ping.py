import urllib.request
tmp = urllib.request.urlopen("https://alkai.netlify.app/", timeout=60)
print(tmp.readlines())
