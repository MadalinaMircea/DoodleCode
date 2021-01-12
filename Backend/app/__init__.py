from flask import Flask
from Business.CodeGeneration.CodeGenerator import CodeGenerator
from IntelligentModels.Detectron2.DetectronUtils import Detectron
from Business.ImageProcessing.ImageUtils import ImageUtils

app = Flask(__name__)

generator = CodeGenerator()
detectron = Detectron()
imageUtils = ImageUtils()

from app import routes
