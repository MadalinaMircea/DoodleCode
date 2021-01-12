from app import app
from app import dogService, basenjiService, corgiService, curService, dalmatianService, greatpyreneesService, griffonService, huntingdogService, lapdogService, leonbergService, mexicanhairlessService, newfoundlandService, poochService, poodleService, pugService, puppyService, spitzService, toydogService, workingdogService
from Classes.Domain.Dog import Dog
from Classes.Domain.Basenji import Basenji
from Classes.Domain.Corgi import Corgi
from Classes.Domain.Cur import Cur
from Classes.Domain.Dalmatian import Dalmatian
from Classes.Domain.GreatPyrenees import GreatPyrenees
from Classes.Domain.Griffon import Griffon
from Classes.Domain.HuntingDog import HuntingDog
from Classes.Domain.Lapdog import Lapdog
from Classes.Domain.Leonberg import Leonberg
from Classes.Domain.MexicanHairless import MexicanHairless
from Classes.Domain.Newfoundland import Newfoundland
from Classes.Domain.Pooch import Pooch
from Classes.Domain.Poodle import Poodle
from Classes.Domain.Pug import Pug
from Classes.Domain.Puppy import Puppy
from Classes.Domain.Spitz import Spitz
from Classes.Domain.ToyDog import ToyDog
from Classes.Domain.WorkingDog import WorkingDog

from flask import request
import json


@app.route('/')
@app.route('/index')
def index():
    return "Hello world!"


@app.route('/add_dog', methods=['POST'])
def add_dog():
    params = request.json
    
    if "description" in params:
        description = params["description"]
    else:
        description = ""

    if dogService.add(description):
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_dog', methods=['POST'])
def update_dog():
    params = request.json
    
    if "description" in params:
        description = params["description"]
    else:
        description = ""

    if dogService.update(description):
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_dog', methods=['POST'])
def delete_dog():
    params = request.json
    
    if "description" in params:
        description = params["description"]
    else:
        description = ""

    if dogService.delete(description):
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_dog', methods=['POST'])
def find_dog():
    params = request.json
    
    if "description" in params:
        description = params["description"]
    else:
        description = ""

    response = dogService.find(description)

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_dog', methods=['POST'])
def get_all_dog():
    response = []

    for elem in dogService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_dog', methods=['POST'])
def size_dog():
    response = dogService.size()

    return json.dumps({"code": 200, "response": response})


@app.route('/add_basenji', methods=['POST'])
def add_basenji():
    params = request.json
    
    if basenjiService.add():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_basenji', methods=['POST'])
def update_basenji():
    params = request.json
    
    if basenjiService.update():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_basenji', methods=['POST'])
def delete_basenji():
    params = request.json
    
    if basenjiService.delete():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_basenji', methods=['POST'])
def find_basenji():
    params = request.json
    
    response = basenjiService.find()

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_basenji', methods=['POST'])
def get_all_basenji():
    response = []

    for elem in basenjiService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_basenji', methods=['POST'])
def size_basenji():
    response = basenjiService.size()

    return json.dumps({"code": 200, "response": response})


@app.route('/add_corgi', methods=['POST'])
def add_corgi():
    params = request.json
    
    if corgiService.add():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_corgi', methods=['POST'])
def update_corgi():
    params = request.json
    
    if corgiService.update():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_corgi', methods=['POST'])
def delete_corgi():
    params = request.json
    
    if corgiService.delete():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_corgi', methods=['POST'])
def find_corgi():
    params = request.json
    
    response = corgiService.find()

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_corgi', methods=['POST'])
def get_all_corgi():
    response = []

    for elem in corgiService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_corgi', methods=['POST'])
def size_corgi():
    response = corgiService.size()

    return json.dumps({"code": 200, "response": response})


@app.route('/add_cur', methods=['POST'])
def add_cur():
    params = request.json
    
    if curService.add():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_cur', methods=['POST'])
def update_cur():
    params = request.json
    
    if curService.update():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_cur', methods=['POST'])
def delete_cur():
    params = request.json
    
    if curService.delete():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_cur', methods=['POST'])
def find_cur():
    params = request.json
    
    response = curService.find()

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_cur', methods=['POST'])
def get_all_cur():
    response = []

    for elem in curService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_cur', methods=['POST'])
def size_cur():
    response = curService.size()

    return json.dumps({"code": 200, "response": response})


@app.route('/add_dalmatian', methods=['POST'])
def add_dalmatian():
    params = request.json
    
    if dalmatianService.add():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_dalmatian', methods=['POST'])
def update_dalmatian():
    params = request.json
    
    if dalmatianService.update():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_dalmatian', methods=['POST'])
def delete_dalmatian():
    params = request.json
    
    if dalmatianService.delete():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_dalmatian', methods=['POST'])
def find_dalmatian():
    params = request.json
    
    response = dalmatianService.find()

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_dalmatian', methods=['POST'])
def get_all_dalmatian():
    response = []

    for elem in dalmatianService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_dalmatian', methods=['POST'])
def size_dalmatian():
    response = dalmatianService.size()

    return json.dumps({"code": 200, "response": response})


@app.route('/add_greatpyrenees', methods=['POST'])
def add_greatpyrenees():
    params = request.json
    
    if greatpyreneesService.add():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_greatpyrenees', methods=['POST'])
def update_greatpyrenees():
    params = request.json
    
    if greatpyreneesService.update():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_greatpyrenees', methods=['POST'])
def delete_greatpyrenees():
    params = request.json
    
    if greatpyreneesService.delete():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_greatpyrenees', methods=['POST'])
def find_greatpyrenees():
    params = request.json
    
    response = greatpyreneesService.find()

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_greatpyrenees', methods=['POST'])
def get_all_greatpyrenees():
    response = []

    for elem in greatpyreneesService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_greatpyrenees', methods=['POST'])
def size_greatpyrenees():
    response = greatpyreneesService.size()

    return json.dumps({"code": 200, "response": response})


@app.route('/add_griffon', methods=['POST'])
def add_griffon():
    params = request.json
    
    if griffonService.add():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_griffon', methods=['POST'])
def update_griffon():
    params = request.json
    
    if griffonService.update():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_griffon', methods=['POST'])
def delete_griffon():
    params = request.json
    
    if griffonService.delete():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_griffon', methods=['POST'])
def find_griffon():
    params = request.json
    
    response = griffonService.find()

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_griffon', methods=['POST'])
def get_all_griffon():
    response = []

    for elem in griffonService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_griffon', methods=['POST'])
def size_griffon():
    response = griffonService.size()

    return json.dumps({"code": 200, "response": response})


@app.route('/add_huntingdog', methods=['POST'])
def add_huntingdog():
    params = request.json
    
    if huntingdogService.add():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_huntingdog', methods=['POST'])
def update_huntingdog():
    params = request.json
    
    if huntingdogService.update():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_huntingdog', methods=['POST'])
def delete_huntingdog():
    params = request.json
    
    if huntingdogService.delete():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_huntingdog', methods=['POST'])
def find_huntingdog():
    params = request.json
    
    response = huntingdogService.find()

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_huntingdog', methods=['POST'])
def get_all_huntingdog():
    response = []

    for elem in huntingdogService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_huntingdog', methods=['POST'])
def size_huntingdog():
    response = huntingdogService.size()

    return json.dumps({"code": 200, "response": response})


@app.route('/add_lapdog', methods=['POST'])
def add_lapdog():
    params = request.json
    
    if lapdogService.add():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_lapdog', methods=['POST'])
def update_lapdog():
    params = request.json
    
    if lapdogService.update():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_lapdog', methods=['POST'])
def delete_lapdog():
    params = request.json
    
    if lapdogService.delete():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_lapdog', methods=['POST'])
def find_lapdog():
    params = request.json
    
    response = lapdogService.find()

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_lapdog', methods=['POST'])
def get_all_lapdog():
    response = []

    for elem in lapdogService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_lapdog', methods=['POST'])
def size_lapdog():
    response = lapdogService.size()

    return json.dumps({"code": 200, "response": response})


@app.route('/add_leonberg', methods=['POST'])
def add_leonberg():
    params = request.json
    
    if leonbergService.add():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_leonberg', methods=['POST'])
def update_leonberg():
    params = request.json
    
    if leonbergService.update():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_leonberg', methods=['POST'])
def delete_leonberg():
    params = request.json
    
    if leonbergService.delete():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_leonberg', methods=['POST'])
def find_leonberg():
    params = request.json
    
    response = leonbergService.find()

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_leonberg', methods=['POST'])
def get_all_leonberg():
    response = []

    for elem in leonbergService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_leonberg', methods=['POST'])
def size_leonberg():
    response = leonbergService.size()

    return json.dumps({"code": 200, "response": response})


@app.route('/add_mexicanhairless', methods=['POST'])
def add_mexicanhairless():
    params = request.json
    
    if mexicanhairlessService.add():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_mexicanhairless', methods=['POST'])
def update_mexicanhairless():
    params = request.json
    
    if mexicanhairlessService.update():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_mexicanhairless', methods=['POST'])
def delete_mexicanhairless():
    params = request.json
    
    if mexicanhairlessService.delete():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_mexicanhairless', methods=['POST'])
def find_mexicanhairless():
    params = request.json
    
    response = mexicanhairlessService.find()

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_mexicanhairless', methods=['POST'])
def get_all_mexicanhairless():
    response = []

    for elem in mexicanhairlessService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_mexicanhairless', methods=['POST'])
def size_mexicanhairless():
    response = mexicanhairlessService.size()

    return json.dumps({"code": 200, "response": response})


@app.route('/add_newfoundland', methods=['POST'])
def add_newfoundland():
    params = request.json
    
    if newfoundlandService.add():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_newfoundland', methods=['POST'])
def update_newfoundland():
    params = request.json
    
    if newfoundlandService.update():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_newfoundland', methods=['POST'])
def delete_newfoundland():
    params = request.json
    
    if newfoundlandService.delete():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_newfoundland', methods=['POST'])
def find_newfoundland():
    params = request.json
    
    response = newfoundlandService.find()

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_newfoundland', methods=['POST'])
def get_all_newfoundland():
    response = []

    for elem in newfoundlandService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_newfoundland', methods=['POST'])
def size_newfoundland():
    response = newfoundlandService.size()

    return json.dumps({"code": 200, "response": response})


@app.route('/add_pooch', methods=['POST'])
def add_pooch():
    params = request.json
    
    if poochService.add():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_pooch', methods=['POST'])
def update_pooch():
    params = request.json
    
    if poochService.update():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_pooch', methods=['POST'])
def delete_pooch():
    params = request.json
    
    if poochService.delete():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_pooch', methods=['POST'])
def find_pooch():
    params = request.json
    
    response = poochService.find()

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_pooch', methods=['POST'])
def get_all_pooch():
    response = []

    for elem in poochService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_pooch', methods=['POST'])
def size_pooch():
    response = poochService.size()

    return json.dumps({"code": 200, "response": response})


@app.route('/add_poodle', methods=['POST'])
def add_poodle():
    params = request.json
    
    if poodleService.add():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_poodle', methods=['POST'])
def update_poodle():
    params = request.json
    
    if poodleService.update():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_poodle', methods=['POST'])
def delete_poodle():
    params = request.json
    
    if poodleService.delete():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_poodle', methods=['POST'])
def find_poodle():
    params = request.json
    
    response = poodleService.find()

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_poodle', methods=['POST'])
def get_all_poodle():
    response = []

    for elem in poodleService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_poodle', methods=['POST'])
def size_poodle():
    response = poodleService.size()

    return json.dumps({"code": 200, "response": response})


@app.route('/add_pug', methods=['POST'])
def add_pug():
    params = request.json
    
    if pugService.add():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_pug', methods=['POST'])
def update_pug():
    params = request.json
    
    if pugService.update():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_pug', methods=['POST'])
def delete_pug():
    params = request.json
    
    if pugService.delete():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_pug', methods=['POST'])
def find_pug():
    params = request.json
    
    response = pugService.find()

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_pug', methods=['POST'])
def get_all_pug():
    response = []

    for elem in pugService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_pug', methods=['POST'])
def size_pug():
    response = pugService.size()

    return json.dumps({"code": 200, "response": response})


@app.route('/add_puppy', methods=['POST'])
def add_puppy():
    params = request.json
    
    if puppyService.add():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_puppy', methods=['POST'])
def update_puppy():
    params = request.json
    
    if puppyService.update():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_puppy', methods=['POST'])
def delete_puppy():
    params = request.json
    
    if puppyService.delete():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_puppy', methods=['POST'])
def find_puppy():
    params = request.json
    
    response = puppyService.find()

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_puppy', methods=['POST'])
def get_all_puppy():
    response = []

    for elem in puppyService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_puppy', methods=['POST'])
def size_puppy():
    response = puppyService.size()

    return json.dumps({"code": 200, "response": response})


@app.route('/add_spitz', methods=['POST'])
def add_spitz():
    params = request.json
    
    if spitzService.add():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_spitz', methods=['POST'])
def update_spitz():
    params = request.json
    
    if spitzService.update():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_spitz', methods=['POST'])
def delete_spitz():
    params = request.json
    
    if spitzService.delete():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_spitz', methods=['POST'])
def find_spitz():
    params = request.json
    
    response = spitzService.find()

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_spitz', methods=['POST'])
def get_all_spitz():
    response = []

    for elem in spitzService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_spitz', methods=['POST'])
def size_spitz():
    response = spitzService.size()

    return json.dumps({"code": 200, "response": response})


@app.route('/add_toydog', methods=['POST'])
def add_toydog():
    params = request.json
    
    if toydogService.add():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_toydog', methods=['POST'])
def update_toydog():
    params = request.json
    
    if toydogService.update():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_toydog', methods=['POST'])
def delete_toydog():
    params = request.json
    
    if toydogService.delete():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_toydog', methods=['POST'])
def find_toydog():
    params = request.json
    
    response = toydogService.find()

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_toydog', methods=['POST'])
def get_all_toydog():
    response = []

    for elem in toydogService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_toydog', methods=['POST'])
def size_toydog():
    response = toydogService.size()

    return json.dumps({"code": 200, "response": response})


@app.route('/add_workingdog', methods=['POST'])
def add_workingdog():
    params = request.json
    
    if workingdogService.add():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/update_workingdog', methods=['POST'])
def update_workingdog():
    params = request.json
    
    if workingdogService.update():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/delete_workingdog', methods=['POST'])
def delete_workingdog():
    params = request.json
    
    if workingdogService.delete():
        code = 200
        response = "OK"
    else:
        code = 504
        response = "Error"

    return json.dumps({"code": code, "response": response})


@app.route('/find_workingdog', methods=['POST'])
def find_workingdog():
    params = request.json
    
    response = workingdogService.find()

    return json.dumps({"code": 200, "response": response})


@app.route('/get_all_workingdog', methods=['POST'])
def get_all_workingdog():
    response = []

    for elem in workingdogService.get_all():
        response.append(elem.serialize())

    return json.dumps({"code": 200, "response": response})


@app.route('/size_workingdog', methods=['POST'])
def size_workingdog():
    response = workingdogService.size()

    return json.dumps({"code": 200, "response": response})
