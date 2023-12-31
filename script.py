import requests
r=requests.get("https:onet.pl")
print(r.status_code)
print(r.ok)
