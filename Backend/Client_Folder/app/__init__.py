from flask import Flask
from Classes.Repository.GuitarRepository import GuitarRepository
from Classes.Service.GuitarService import GuitarService


app = Flask(__name__)

guitarRepo = GuitarRepository()
guitarService = GuitarService(guitarRepo)


from app import routes
