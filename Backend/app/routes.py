from app import app, generator
from flask import request
import json


@app.route('/')
@app.route('/index')
def index():
    return "Hello world!"


@app.route('/generate_code', methods=['POST'])
def generate_code():
    params = request.json

    code = 200

    if "doodle" not in params:
        return json.dumps({"code": 504, "response": "Doodle not found."})

    doodle = params["doodle"]

    if "pars_funcs" not in params:
        return json.dumps({"code": 504, "response": "Parameters and Functions not found."})

    pars_funcs = params["pars_funcs"]

    if "output_file" not in params:
        return json.dumps({"code": 504, "response": "Output file not found."})

    output_file = params["output_file"]

    print(doodle)
    print(pars_funcs)
    print(output_file)

    correct, error = generator.generate_code(doodle, pars_funcs, output_file)

    if not correct:
        code = 504

    return json.dumps({"code": code, "response": error})
