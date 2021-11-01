from flask import Flask, request, jsonify
from pymodm import connect, MongoModel, fields


app = Flask(__name__)


def initialize_server():
    print("connecting to MongoDB...")
    connect("mongodb+srv://amey:fanyuan@cluster0.dovib.mongodb.net/"+
            "HealthDatabase?retryWrites=true&w=majority")
    print("Successful!")


class Patients(MongoModel):
    name = fields.CharField()
    id = fields.IntegerField(primary_key=True)
    bloodtype = fields.CharField()
    tests = fields.ListField()


@app.route("/", methods=["GET"])
def status():
    return "Server is On"


@app.route("/new_patient", methods=["POST"])
def new_patient():
    in_data = request.get_json()

    expected_types = {"name": str, "id": int, "blood_type": str}
    error_string, status = validate_server_input(in_data, expected_types)
    if error_string:
        return error_string, status

    new_patient = add_database_entry(in_data["name"], 
                       in_data["id"], in_data["blood_type"])
    return "Added patient {}".format(new_patient)


@app.route("/add_test", methods=["POST"])
def new_test():
    in_data = request.get_json()

    expected_types = {"id": int, "test_name": str, "test_result": int}
    error_string, status = validate_server_input(in_data, expected_types)
    if error_string:
        return error_string, status

    patient = add_test_entry(in_data["id"], 
                       in_data["test_name"], in_data["test_result"])
    return "Updated patient {}".format(patient["ID"])


def add_database_entry(patient_name, id_no, blood_type):
    new_patient = Patients(name=patient_name,
                          id=id_no,
                          bloodtype=blood_type)
    answer = new_patient.save()
    return answer


def add_test_entry(id, test_name, test_result):
    patient = retrieve_patient_by_id(id)
    patient["Tests"].append((test_name, test_result))
    return patient


def retrieve_patient_by_id(id):
    for patient in db:
        if patient['ID'] == id:
            return patient


def validate_server_input(in_data, expected_types):
    if type(in_data) is not dict:
        return "Input was not a dictionary.", 400

    for key in expected_types:
        if key not in in_data:
            return "The key {} is not in input.".format(key), 400
        if type(in_data[key]) is not expected_types[key]:
            return "Wrong datatype for key '{}' in input.".format(key), 400

    return False, 200


if __name__ == "__main__":
    initialize_server()
    app.run()