from flask import Flask, jsonify

app = Flask(__name__)

data = {
    "status": "success",
    "data": [
        {"id": 1, "employee_name": "Tiger Nixon", "employee_salary": 320800, "employee_age": 61, "profile_image": ""}
    ],
    "message": "Successfully! All records has been fetched."
}

@app.route('/api/employees', methods=['GET'])
def get_employees():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
