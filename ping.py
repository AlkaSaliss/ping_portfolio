import urllib.request
tmp1 = urllib.request.urlopen("https://alkai.herokuapp.com", timeout=60)
tmp2 = urllib.request.urlopen("https://alkai.netlify.app", timeout=60)


print(tmp1.readlines())
print(tmp2.readlines())
