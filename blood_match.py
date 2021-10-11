import requests

server = 'http://vcm-7631.vm.duke.edu:5002/'

r_amey = requests.get(server+"get_patients/aac55")
amey_json = r_amey.json()
print(amey_json)

r_hillel = requests.get(server+"get_patients/hp48")
hillel_json = r_hillel.json()
print(hillel_json)

amey_id = amey_json["Recipient"]
hillel_id = hillel_json["Donor"]

r_blood_type_amey = requests.get(server+"get_blood_type/"+amey_id)
print(r_blood_type_amey.text)

r_blood_type_hillel = requests.get(server+"get_blood_type/"+hillel_id)
print(r_blood_type_hillel.text)

match_json = {'Name': 'aac55', "Match": "Yes"}
r = requests.post(server+"match_check", json=match_json)
print(r.text)


