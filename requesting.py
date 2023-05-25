import requests

# Make a GET request to the specified URL with the given parameters
r = requests.request("GET", url="http://127.0.0.1:5000/location", params={"loc_x": 10.2, "loc_y": 11})

# Print the content of the response
print(r.content)


# Make a POST request to the specified URL with the given parameters
p = requests.request("POST", url="http://127.0.0.1:5000/violation", params={"id": 1, "name": "Harsh", "lic": 4321, "timestamp": "10:22:13", "loc_x": 43.12, "loc_y": 93.48})
