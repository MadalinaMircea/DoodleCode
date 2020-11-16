from app import app
from app import guitarService
from Classes.Domain.Guitar import Guitar

from flask import request
import json


@app.route('/')
@app.route('/index')
def index():
    return "Hello world!"


@app.route('/add_guitar', methods=['POST'])
def add_guitar():
    params = request.json
    
    if guitarService.add():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_guitar', methods=['POST'])
def update_guitar():
    params = request.json
    
    if guitarService.update():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_guitar', methods=['POST'])
def delete_guitar():
    params = request.json
    
    if guitarService.delete():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_guitar', methods=['POST'])
def find_guitar():
    params = request.json
    
    response = guitarService.find()

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_guitar', methods=['POST'])
def get_all_guitar():
    response = []

    for elem in guitarService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_guitar', methods=['POST'])
def size_guitar():
    response = guitarService.size()

    return json.dumps({"code": 200, "response": response})
