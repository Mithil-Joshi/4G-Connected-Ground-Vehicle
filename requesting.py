import requests


r = requests.request("GET", url="http://127.0.0.1:5000/location", params={"loc_x":10.2, "loc_y":11})
print(r.content)