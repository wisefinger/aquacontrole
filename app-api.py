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


if __name__ == '__main__':
    app.run(debug=True)
