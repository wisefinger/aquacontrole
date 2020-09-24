# this python program will contain the code for a api controller
from flask import Flask, redirect, render_template, request, url_for, jsonify

app = Flask(__name__)



sensor_list = [
    {
        "id" : 0,
        "name" : "sensor1" ,
        "type" : "temperature"

    },
    {
        "id": 1,
        "name": "sensor2",
        "type": "temperature"

    },
    {
        "id": 2,
        "name": "senjsor3",
        "type": "TDS"

    }
    ]


@app.route('/sensors', methods=['GET', 'POST'] )
def sensors():
    if request.method == 'GET':
        if len(sensor_list) > 0:
            return jsonify(sensor_list)
        else:
            'Nothing Found', 404

    if request.method == 'POST':
        new_id = request.form['id']
        new_name = request.form['name']
        new_type = request.form['type']

        new_sensor = {
            'id' : new_id,
            'name' : new_name,
            'type': new_type
        }
    sensor_list.append(new_sensor)
    return  jsonify(sensor_list), 201

if __name__ == '__main__':
    app.run(debug=True)
