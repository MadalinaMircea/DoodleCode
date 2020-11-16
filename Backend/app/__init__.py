from flask import Flask
from CodeGenerator import CodeGenerator

app = Flask(__name__)

generator = CodeGenerator()

from app import routes
