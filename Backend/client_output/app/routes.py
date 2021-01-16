from app import app
from app import birdService, apodiformbirdService, aquaticbirdService, archaeopteryxService, archaeornisService, birdofpassageService, birdofpreyService, caprimulgiformbirdService, carinateService, cockService, coraciiformbirdService, cuculiformbirdService, dickeybirdService, gallinaceousbirdService, henService, iberomesornisService, nesterService, nightbirdService, nonpasserinebirdService, parrotService, passerineService, piciformbirdService, protoavisService, ratiteService, sinornisService, trogonService, twittererService
from Classes.Domain.Bird import Bird
from Classes.Domain.ApodiformBird import ApodiformBird
from Classes.Domain.AquaticBird import AquaticBird
from Classes.Domain.Archaeopteryx import Archaeopteryx
from Classes.Domain.Archaeornis import Archaeornis
from Classes.Domain.BirdOfPassage import BirdOfPassage
from Classes.Domain.BirdOfPrey import BirdOfPrey
from Classes.Domain.CaprimulgiformBird import CaprimulgiformBird
from Classes.Domain.Carinate import Carinate
from Classes.Domain.Cock import Cock
from Classes.Domain.CoraciiformBird import CoraciiformBird
from Classes.Domain.CuculiformBird import CuculiformBird
from Classes.Domain.Dickeybird import Dickeybird
from Classes.Domain.GallinaceousBird import GallinaceousBird
from Classes.Domain.Hen import Hen
from Classes.Domain.IberoMesornis import IberoMesornis
from Classes.Domain.Nester import Nester
from Classes.Domain.NightBird import NightBird
from Classes.Domain.NonpasserineBird import NonpasserineBird
from Classes.Domain.Parrot import Parrot
from Classes.Domain.Passerine import Passerine
from Classes.Domain.PiciformBird import PiciformBird
from Classes.Domain.Protoavis import Protoavis
from Classes.Domain.Ratite import Ratite
from Classes.Domain.Sinornis import Sinornis
from Classes.Domain.Trogon import Trogon
from Classes.Domain.Twitterer import Twitterer

from flask import request
import json


@app.route('/')
@app.route('/index')
def index():
    return "Hello world!"


@app.route('/add_bird', methods=['POST'])
def add_bird():
    params = request.json
    
    if "description" in params:
        description = params["description"]
    else:
        description = ""

    if birdService.add(description):
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_bird', methods=['POST'])
def update_bird():
    params = request.json
    
    if "description" in params:
        description = params["description"]
    else:
        description = ""

    if birdService.update(description):
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_bird', methods=['POST'])
def delete_bird():
    params = request.json
    
    if "description" in params:
        description = params["description"]
    else:
        description = ""

    if birdService.delete(description):
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_bird', methods=['POST'])
def find_bird():
    params = request.json
    
    if "description" in params:
        description = params["description"]
    else:
        description = ""

    response = birdService.find(description)

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_bird', methods=['POST'])
def get_all_bird():
    response = []

    for elem in birdService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_bird', methods=['POST'])
def size_bird():
    response = birdService.size()

    return json.dumps({"code": 200, "response": response})


@app.route('/add_apodiformbird', methods=['POST'])
def add_apodiformbird():
    params = request.json
    
    if apodiformbirdService.add():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_apodiformbird', methods=['POST'])
def update_apodiformbird():
    params = request.json
    
    if apodiformbirdService.update():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_apodiformbird', methods=['POST'])
def delete_apodiformbird():
    params = request.json
    
    if apodiformbirdService.delete():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_apodiformbird', methods=['POST'])
def find_apodiformbird():
    params = request.json
    
    response = apodiformbirdService.find()

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_apodiformbird', methods=['POST'])
def get_all_apodiformbird():
    response = []

    for elem in apodiformbirdService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_apodiformbird', methods=['POST'])
def size_apodiformbird():
    response = apodiformbirdService.size()

    return json.dumps({"code": 200, "response": response})


@app.route('/add_aquaticbird', methods=['POST'])
def add_aquaticbird():
    params = request.json
    
    if aquaticbirdService.add():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_aquaticbird', methods=['POST'])
def update_aquaticbird():
    params = request.json
    
    if aquaticbirdService.update():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_aquaticbird', methods=['POST'])
def delete_aquaticbird():
    params = request.json
    
    if aquaticbirdService.delete():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_aquaticbird', methods=['POST'])
def find_aquaticbird():
    params = request.json
    
    response = aquaticbirdService.find()

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_aquaticbird', methods=['POST'])
def get_all_aquaticbird():
    response = []

    for elem in aquaticbirdService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_aquaticbird', methods=['POST'])
def size_aquaticbird():
    response = aquaticbirdService.size()

    return json.dumps({"code": 200, "response": response})


@app.route('/add_archaeopteryx', methods=['POST'])
def add_archaeopteryx():
    params = request.json
    
    if archaeopteryxService.add():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_archaeopteryx', methods=['POST'])
def update_archaeopteryx():
    params = request.json
    
    if archaeopteryxService.update():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_archaeopteryx', methods=['POST'])
def delete_archaeopteryx():
    params = request.json
    
    if archaeopteryxService.delete():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_archaeopteryx', methods=['POST'])
def find_archaeopteryx():
    params = request.json
    
    response = archaeopteryxService.find()

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_archaeopteryx', methods=['POST'])
def get_all_archaeopteryx():
    response = []

    for elem in archaeopteryxService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_archaeopteryx', methods=['POST'])
def size_archaeopteryx():
    response = archaeopteryxService.size()

    return json.dumps({"code": 200, "response": response})


@app.route('/add_archaeornis', methods=['POST'])
def add_archaeornis():
    params = request.json
    
    if archaeornisService.add():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_archaeornis', methods=['POST'])
def update_archaeornis():
    params = request.json
    
    if archaeornisService.update():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_archaeornis', methods=['POST'])
def delete_archaeornis():
    params = request.json
    
    if archaeornisService.delete():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_archaeornis', methods=['POST'])
def find_archaeornis():
    params = request.json
    
    response = archaeornisService.find()

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_archaeornis', methods=['POST'])
def get_all_archaeornis():
    response = []

    for elem in archaeornisService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_archaeornis', methods=['POST'])
def size_archaeornis():
    response = archaeornisService.size()

    return json.dumps({"code": 200, "response": response})


@app.route('/add_birdofpassage', methods=['POST'])
def add_birdofpassage():
    params = request.json
    
    if birdofpassageService.add():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_birdofpassage', methods=['POST'])
def update_birdofpassage():
    params = request.json
    
    if birdofpassageService.update():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_birdofpassage', methods=['POST'])
def delete_birdofpassage():
    params = request.json
    
    if birdofpassageService.delete():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_birdofpassage', methods=['POST'])
def find_birdofpassage():
    params = request.json
    
    response = birdofpassageService.find()

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_birdofpassage', methods=['POST'])
def get_all_birdofpassage():
    response = []

    for elem in birdofpassageService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_birdofpassage', methods=['POST'])
def size_birdofpassage():
    response = birdofpassageService.size()

    return json.dumps({"code": 200, "response": response})


@app.route('/add_birdofprey', methods=['POST'])
def add_birdofprey():
    params = request.json
    
    if birdofpreyService.add():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_birdofprey', methods=['POST'])
def update_birdofprey():
    params = request.json
    
    if birdofpreyService.update():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_birdofprey', methods=['POST'])
def delete_birdofprey():
    params = request.json
    
    if birdofpreyService.delete():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_birdofprey', methods=['POST'])
def find_birdofprey():
    params = request.json
    
    response = birdofpreyService.find()

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_birdofprey', methods=['POST'])
def get_all_birdofprey():
    response = []

    for elem in birdofpreyService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_birdofprey', methods=['POST'])
def size_birdofprey():
    response = birdofpreyService.size()

    return json.dumps({"code": 200, "response": response})


@app.route('/add_caprimulgiformbird', methods=['POST'])
def add_caprimulgiformbird():
    params = request.json
    
    if caprimulgiformbirdService.add():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_caprimulgiformbird', methods=['POST'])
def update_caprimulgiformbird():
    params = request.json
    
    if caprimulgiformbirdService.update():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_caprimulgiformbird', methods=['POST'])
def delete_caprimulgiformbird():
    params = request.json
    
    if caprimulgiformbirdService.delete():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_caprimulgiformbird', methods=['POST'])
def find_caprimulgiformbird():
    params = request.json
    
    response = caprimulgiformbirdService.find()

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_caprimulgiformbird', methods=['POST'])
def get_all_caprimulgiformbird():
    response = []

    for elem in caprimulgiformbirdService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_caprimulgiformbird', methods=['POST'])
def size_caprimulgiformbird():
    response = caprimulgiformbirdService.size()

    return json.dumps({"code": 200, "response": response})


@app.route('/add_carinate', methods=['POST'])
def add_carinate():
    params = request.json
    
    if carinateService.add():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_carinate', methods=['POST'])
def update_carinate():
    params = request.json
    
    if carinateService.update():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_carinate', methods=['POST'])
def delete_carinate():
    params = request.json
    
    if carinateService.delete():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_carinate', methods=['POST'])
def find_carinate():
    params = request.json
    
    response = carinateService.find()

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_carinate', methods=['POST'])
def get_all_carinate():
    response = []

    for elem in carinateService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_carinate', methods=['POST'])
def size_carinate():
    response = carinateService.size()

    return json.dumps({"code": 200, "response": response})


@app.route('/add_cock', methods=['POST'])
def add_cock():
    params = request.json
    
    if cockService.add():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_cock', methods=['POST'])
def update_cock():
    params = request.json
    
    if cockService.update():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_cock', methods=['POST'])
def delete_cock():
    params = request.json
    
    if cockService.delete():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_cock', methods=['POST'])
def find_cock():
    params = request.json
    
    response = cockService.find()

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_cock', methods=['POST'])
def get_all_cock():
    response = []

    for elem in cockService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_cock', methods=['POST'])
def size_cock():
    response = cockService.size()

    return json.dumps({"code": 200, "response": response})


@app.route('/add_coraciiformbird', methods=['POST'])
def add_coraciiformbird():
    params = request.json
    
    if coraciiformbirdService.add():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_coraciiformbird', methods=['POST'])
def update_coraciiformbird():
    params = request.json
    
    if coraciiformbirdService.update():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_coraciiformbird', methods=['POST'])
def delete_coraciiformbird():
    params = request.json
    
    if coraciiformbirdService.delete():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_coraciiformbird', methods=['POST'])
def find_coraciiformbird():
    params = request.json
    
    response = coraciiformbirdService.find()

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_coraciiformbird', methods=['POST'])
def get_all_coraciiformbird():
    response = []

    for elem in coraciiformbirdService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_coraciiformbird', methods=['POST'])
def size_coraciiformbird():
    response = coraciiformbirdService.size()

    return json.dumps({"code": 200, "response": response})


@app.route('/add_cuculiformbird', methods=['POST'])
def add_cuculiformbird():
    params = request.json
    
    if cuculiformbirdService.add():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_cuculiformbird', methods=['POST'])
def update_cuculiformbird():
    params = request.json
    
    if cuculiformbirdService.update():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_cuculiformbird', methods=['POST'])
def delete_cuculiformbird():
    params = request.json
    
    if cuculiformbirdService.delete():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_cuculiformbird', methods=['POST'])
def find_cuculiformbird():
    params = request.json
    
    response = cuculiformbirdService.find()

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_cuculiformbird', methods=['POST'])
def get_all_cuculiformbird():
    response = []

    for elem in cuculiformbirdService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_cuculiformbird', methods=['POST'])
def size_cuculiformbird():
    response = cuculiformbirdService.size()

    return json.dumps({"code": 200, "response": response})


@app.route('/add_dickeybird', methods=['POST'])
def add_dickeybird():
    params = request.json
    
    if dickeybirdService.add():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_dickeybird', methods=['POST'])
def update_dickeybird():
    params = request.json
    
    if dickeybirdService.update():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_dickeybird', methods=['POST'])
def delete_dickeybird():
    params = request.json
    
    if dickeybirdService.delete():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_dickeybird', methods=['POST'])
def find_dickeybird():
    params = request.json
    
    response = dickeybirdService.find()

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_dickeybird', methods=['POST'])
def get_all_dickeybird():
    response = []

    for elem in dickeybirdService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_dickeybird', methods=['POST'])
def size_dickeybird():
    response = dickeybirdService.size()

    return json.dumps({"code": 200, "response": response})


@app.route('/add_gallinaceousbird', methods=['POST'])
def add_gallinaceousbird():
    params = request.json
    
    if gallinaceousbirdService.add():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_gallinaceousbird', methods=['POST'])
def update_gallinaceousbird():
    params = request.json
    
    if gallinaceousbirdService.update():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_gallinaceousbird', methods=['POST'])
def delete_gallinaceousbird():
    params = request.json
    
    if gallinaceousbirdService.delete():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_gallinaceousbird', methods=['POST'])
def find_gallinaceousbird():
    params = request.json
    
    response = gallinaceousbirdService.find()

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_gallinaceousbird', methods=['POST'])
def get_all_gallinaceousbird():
    response = []

    for elem in gallinaceousbirdService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_gallinaceousbird', methods=['POST'])
def size_gallinaceousbird():
    response = gallinaceousbirdService.size()

    return json.dumps({"code": 200, "response": response})


@app.route('/add_hen', methods=['POST'])
def add_hen():
    params = request.json
    
    if henService.add():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_hen', methods=['POST'])
def update_hen():
    params = request.json
    
    if henService.update():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_hen', methods=['POST'])
def delete_hen():
    params = request.json
    
    if henService.delete():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_hen', methods=['POST'])
def find_hen():
    params = request.json
    
    response = henService.find()

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_hen', methods=['POST'])
def get_all_hen():
    response = []

    for elem in henService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_hen', methods=['POST'])
def size_hen():
    response = henService.size()

    return json.dumps({"code": 200, "response": response})


@app.route('/add_iberomesornis', methods=['POST'])
def add_iberomesornis():
    params = request.json
    
    if iberomesornisService.add():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_iberomesornis', methods=['POST'])
def update_iberomesornis():
    params = request.json
    
    if iberomesornisService.update():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_iberomesornis', methods=['POST'])
def delete_iberomesornis():
    params = request.json
    
    if iberomesornisService.delete():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_iberomesornis', methods=['POST'])
def find_iberomesornis():
    params = request.json
    
    response = iberomesornisService.find()

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_iberomesornis', methods=['POST'])
def get_all_iberomesornis():
    response = []

    for elem in iberomesornisService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_iberomesornis', methods=['POST'])
def size_iberomesornis():
    response = iberomesornisService.size()

    return json.dumps({"code": 200, "response": response})


@app.route('/add_nester', methods=['POST'])
def add_nester():
    params = request.json
    
    if nesterService.add():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_nester', methods=['POST'])
def update_nester():
    params = request.json
    
    if nesterService.update():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_nester', methods=['POST'])
def delete_nester():
    params = request.json
    
    if nesterService.delete():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_nester', methods=['POST'])
def find_nester():
    params = request.json
    
    response = nesterService.find()

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_nester', methods=['POST'])
def get_all_nester():
    response = []

    for elem in nesterService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_nester', methods=['POST'])
def size_nester():
    response = nesterService.size()

    return json.dumps({"code": 200, "response": response})


@app.route('/add_nightbird', methods=['POST'])
def add_nightbird():
    params = request.json
    
    if nightbirdService.add():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_nightbird', methods=['POST'])
def update_nightbird():
    params = request.json
    
    if nightbirdService.update():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_nightbird', methods=['POST'])
def delete_nightbird():
    params = request.json
    
    if nightbirdService.delete():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_nightbird', methods=['POST'])
def find_nightbird():
    params = request.json
    
    response = nightbirdService.find()

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_nightbird', methods=['POST'])
def get_all_nightbird():
    response = []

    for elem in nightbirdService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_nightbird', methods=['POST'])
def size_nightbird():
    response = nightbirdService.size()

    return json.dumps({"code": 200, "response": response})


@app.route('/add_nonpasserinebird', methods=['POST'])
def add_nonpasserinebird():
    params = request.json
    
    if nonpasserinebirdService.add():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_nonpasserinebird', methods=['POST'])
def update_nonpasserinebird():
    params = request.json
    
    if nonpasserinebirdService.update():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_nonpasserinebird', methods=['POST'])
def delete_nonpasserinebird():
    params = request.json
    
    if nonpasserinebirdService.delete():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_nonpasserinebird', methods=['POST'])
def find_nonpasserinebird():
    params = request.json
    
    response = nonpasserinebirdService.find()

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_nonpasserinebird', methods=['POST'])
def get_all_nonpasserinebird():
    response = []

    for elem in nonpasserinebirdService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_nonpasserinebird', methods=['POST'])
def size_nonpasserinebird():
    response = nonpasserinebirdService.size()

    return json.dumps({"code": 200, "response": response})


@app.route('/add_parrot', methods=['POST'])
def add_parrot():
    params = request.json
    
    if parrotService.add():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_parrot', methods=['POST'])
def update_parrot():
    params = request.json
    
    if parrotService.update():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_parrot', methods=['POST'])
def delete_parrot():
    params = request.json
    
    if parrotService.delete():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_parrot', methods=['POST'])
def find_parrot():
    params = request.json
    
    response = parrotService.find()

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_parrot', methods=['POST'])
def get_all_parrot():
    response = []

    for elem in parrotService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_parrot', methods=['POST'])
def size_parrot():
    response = parrotService.size()

    return json.dumps({"code": 200, "response": response})


@app.route('/add_passerine', methods=['POST'])
def add_passerine():
    params = request.json
    
    if passerineService.add():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_passerine', methods=['POST'])
def update_passerine():
    params = request.json
    
    if passerineService.update():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_passerine', methods=['POST'])
def delete_passerine():
    params = request.json
    
    if passerineService.delete():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_passerine', methods=['POST'])
def find_passerine():
    params = request.json
    
    response = passerineService.find()

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_passerine', methods=['POST'])
def get_all_passerine():
    response = []

    for elem in passerineService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_passerine', methods=['POST'])
def size_passerine():
    response = passerineService.size()

    return json.dumps({"code": 200, "response": response})


@app.route('/add_piciformbird', methods=['POST'])
def add_piciformbird():
    params = request.json
    
    if piciformbirdService.add():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_piciformbird', methods=['POST'])
def update_piciformbird():
    params = request.json
    
    if piciformbirdService.update():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_piciformbird', methods=['POST'])
def delete_piciformbird():
    params = request.json
    
    if piciformbirdService.delete():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_piciformbird', methods=['POST'])
def find_piciformbird():
    params = request.json
    
    response = piciformbirdService.find()

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_piciformbird', methods=['POST'])
def get_all_piciformbird():
    response = []

    for elem in piciformbirdService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_piciformbird', methods=['POST'])
def size_piciformbird():
    response = piciformbirdService.size()

    return json.dumps({"code": 200, "response": response})


@app.route('/add_protoavis', methods=['POST'])
def add_protoavis():
    params = request.json
    
    if protoavisService.add():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_protoavis', methods=['POST'])
def update_protoavis():
    params = request.json
    
    if protoavisService.update():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_protoavis', methods=['POST'])
def delete_protoavis():
    params = request.json
    
    if protoavisService.delete():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_protoavis', methods=['POST'])
def find_protoavis():
    params = request.json
    
    response = protoavisService.find()

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_protoavis', methods=['POST'])
def get_all_protoavis():
    response = []

    for elem in protoavisService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_protoavis', methods=['POST'])
def size_protoavis():
    response = protoavisService.size()

    return json.dumps({"code": 200, "response": response})


@app.route('/add_ratite', methods=['POST'])
def add_ratite():
    params = request.json
    
    if ratiteService.add():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_ratite', methods=['POST'])
def update_ratite():
    params = request.json
    
    if ratiteService.update():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_ratite', methods=['POST'])
def delete_ratite():
    params = request.json
    
    if ratiteService.delete():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_ratite', methods=['POST'])
def find_ratite():
    params = request.json
    
    response = ratiteService.find()

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_ratite', methods=['POST'])
def get_all_ratite():
    response = []

    for elem in ratiteService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_ratite', methods=['POST'])
def size_ratite():
    response = ratiteService.size()

    return json.dumps({"code": 200, "response": response})


@app.route('/add_sinornis', methods=['POST'])
def add_sinornis():
    params = request.json
    
    if sinornisService.add():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_sinornis', methods=['POST'])
def update_sinornis():
    params = request.json
    
    if sinornisService.update():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_sinornis', methods=['POST'])
def delete_sinornis():
    params = request.json
    
    if sinornisService.delete():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_sinornis', methods=['POST'])
def find_sinornis():
    params = request.json
    
    response = sinornisService.find()

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_sinornis', methods=['POST'])
def get_all_sinornis():
    response = []

    for elem in sinornisService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_sinornis', methods=['POST'])
def size_sinornis():
    response = sinornisService.size()

    return json.dumps({"code": 200, "response": response})


@app.route('/add_trogon', methods=['POST'])
def add_trogon():
    params = request.json
    
    if trogonService.add():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_trogon', methods=['POST'])
def update_trogon():
    params = request.json
    
    if trogonService.update():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_trogon', methods=['POST'])
def delete_trogon():
    params = request.json
    
    if trogonService.delete():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_trogon', methods=['POST'])
def find_trogon():
    params = request.json
    
    response = trogonService.find()

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_trogon', methods=['POST'])
def get_all_trogon():
    response = []

    for elem in trogonService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_trogon', methods=['POST'])
def size_trogon():
    response = trogonService.size()

    return json.dumps({"code": 200, "response": response})


@app.route('/add_twitterer', methods=['POST'])
def add_twitterer():
    params = request.json
    
    if twittererService.add():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_twitterer', methods=['POST'])
def update_twitterer():
    params = request.json
    
    if twittererService.update():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_twitterer', methods=['POST'])
def delete_twitterer():
    params = request.json
    
    if twittererService.delete():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_twitterer', methods=['POST'])
def find_twitterer():
    params = request.json
    
    response = twittererService.find()

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_twitterer', methods=['POST'])
def get_all_twitterer():
    response = []

    for elem in twittererService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_twitterer', methods=['POST'])
def size_twitterer():
    response = twittererService.size()

    return json.dumps({"code": 200, "response": response})
