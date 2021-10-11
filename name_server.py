import requests

server_name = 'http://vcm-21170.vm.duke.edu:5000/'

request_json = {
   "name": "Amey Chaware",
   "net_id": "aac55",
   "e-mail": "amey.chaware@duke.edu"
}

r = requests.post(server_name+"student", json=request_json)
if r.status_code != 200:
    print(r.text)
else:
    print(r.json())

r = requests.get(server_name + "list")
if r.status_code != 200:
    print(r.text)
else:
    print(r.json())


new_json = {"a": 4,
            "b": 3}
r = requests.post(server_name+"sum", json=new_json)
if r.status_code != 200:
    print(r.text)
else:
    print(r.json())