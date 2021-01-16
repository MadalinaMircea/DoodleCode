from app import app, generator, detectron, imageUtils
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

    # if "doodle" not in params:
    #     return json.dumps({"code": 504, "response": "Doodle not found."})
    #
    # doodle = params["doodle"]

    # if "pars_funcs" not in params:
    #     return json.dumps({"code": 504, "response": "Parameters and Functions not found."})

    # pars_funcs = params["pars_funcs"]

    if "classes" not in params:
        return json.dumps({"code": 504, "response": "Classes not found."})

    classes = params["classes"]

    if "output_file" not in params:
        return json.dumps({"code": 504, "response": "Output file not found."})

    output_file = params["output_file"]

    correct, error = generator.generate_code(list(dict.fromkeys(classes)), output_file)

    if not correct:
        code = 504

    return json.dumps({"code": code, "response": error})


@app.route('/get_objects', methods=['POST'])
def get_objects():
    params = request.json

    code = 200

    if "image_bytes" not in params:
        return json.dumps({"code": 504, "response": "Image information not found."})

    image = params["image_bytes"]

    imageUtils.bytes_to_image(image, "Data/received.png")

    detected = list(dict.fromkeys(detectron.detect_masks("Data/received.png", "Data/output.png", 0.2)))

    return json.dumps({"code": code, "response": {"detected": detected}})
