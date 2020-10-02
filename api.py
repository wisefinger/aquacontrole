# this python program will contain the code for a api controller
from flask import Flask, redirect, render_template, request, url_for, jsonify
from utils.TempSensor import TempSensor
from utils.Pump import Pump

app = Flask(__name__)

# code to handle datastream calls
@app.route('/datastream/<int:id>', methods=['GET'] )
def datastream(id):
        if request.method == 'GET':
                      
            sensor = TempSensor(f'{id}')
            datastream = sensor.getTemp()
            if len(datastream) > 0:
                return jsonify(datastream)
            else:
                'Nothing Found', 404
            datastream.close()
            
# code to handle pump actions
@app.route('/pumpaction/<int:duration>', methods=['GET'] )
def pumpaction(duration):
       if request.method == 'GET':
                      
            if (duration) > 0:
                
                pump = Pump()
                pump.waterchange(duration)
                pump.close()
                               
                return f'pump started for {duration} seconds'
            else:
                'Nothing Found', 404
            

# example code
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



@app.route('/sensor/<int:id>', methods=['GET', 'PUT','DELETE'])
def single_sensor(id):
    if request.method == 'GET':
        for sensor in sensor_list:
            if sensor['id'] == id:
                return jsonify(sensor)
            pass
    if request.method == 'PUT':
        for sensor in sensor_list:
            if sensor['id'] == id:
                sensor['id'] =request.form['id'],
                sensor['name'] = request.form['name'],
                sensor['type'] = request.form['type']
                updated_sensor = {
                 'id': sensor['id'],
                 'name': sensor['name'],
                 'type': sensor['type']
                }
                return jsonify(updated_sensor)

    if request.method == 'DELETE':
        for index, sensor in enumerate(sensor_list):
            if sensor['id'] == id:
                sensor_list.pop(index)
                return jsonify(sensor_list)
            
            
@app.route('/sensors', methods=['GET', 'POST'] )
def sensors():
    if request.method == 'GET':
        print(f'>> tempsensor 1 = {tempsensor_1.getTemp()}')
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
