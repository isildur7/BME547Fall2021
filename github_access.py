import requests

server_name = "https://api.github.com/"

r = requests.get(server_name + "repos/isildur7/BME547Fall2021/branches")

print(r)
print(type(r))
print(r.status_code)
print(r.text)

branches = r.json()
print(type(branches))