import requests

patient1 = {"name": "Ann Ables",
            "id": 255,
            "blood_type": "O-"}
r = requests.post("http://127.0.0.1:5000/new_patient", json=patient1)
print(r.status_code)
print(r.text)

# patient1_t = {"id": 255, "test_name": "HDL", "test_result": 130}
# r = requests.post("http://127.0.0.1:5000/add_test", json=patient1_t)
# print(r.status_code)
# print(r.text)