from flask import Flask
from Classes.Repository.BirdRepository import BirdRepository
from Classes.Repository.ApodiformbirdRepository import ApodiformbirdRepository
from Classes.Repository.AquaticbirdRepository import AquaticbirdRepository
from Classes.Repository.ArchaeopteryxRepository import ArchaeopteryxRepository
from Classes.Repository.ArchaeornisRepository import ArchaeornisRepository
from Classes.Repository.BirdofpassageRepository import BirdofpassageRepository
from Classes.Repository.BirdofpreyRepository import BirdofpreyRepository
from Classes.Repository.CaprimulgiformbirdRepository import CaprimulgiformbirdRepository
from Classes.Repository.CarinateRepository import CarinateRepository
from Classes.Repository.CockRepository import CockRepository
from Classes.Repository.CoraciiformbirdRepository import CoraciiformbirdRepository
from Classes.Repository.CuculiformbirdRepository import CuculiformbirdRepository
from Classes.Repository.DickeybirdRepository import DickeybirdRepository
from Classes.Repository.GallinaceousbirdRepository import GallinaceousbirdRepository
from Classes.Repository.HenRepository import HenRepository
from Classes.Repository.IberomesornisRepository import IberomesornisRepository
from Classes.Repository.NesterRepository import NesterRepository
from Classes.Repository.NightbirdRepository import NightbirdRepository
from Classes.Repository.NonpasserinebirdRepository import NonpasserinebirdRepository
from Classes.Repository.ParrotRepository import ParrotRepository
from Classes.Repository.PasserineRepository import PasserineRepository
from Classes.Repository.PiciformbirdRepository import PiciformbirdRepository
from Classes.Repository.ProtoavisRepository import ProtoavisRepository
from Classes.Repository.RatiteRepository import RatiteRepository
from Classes.Repository.SinornisRepository import SinornisRepository
from Classes.Repository.TrogonRepository import TrogonRepository
from Classes.Repository.TwittererRepository import TwittererRepository
from Classes.Service.BirdService import BirdService
from Classes.Service.ApodiformbirdService import ApodiformbirdService
from Classes.Service.AquaticbirdService import AquaticbirdService
from Classes.Service.ArchaeopteryxService import ArchaeopteryxService
from Classes.Service.ArchaeornisService import ArchaeornisService
from Classes.Service.BirdofpassageService import BirdofpassageService
from Classes.Service.BirdofpreyService import BirdofpreyService
from Classes.Service.CaprimulgiformbirdService import CaprimulgiformbirdService
from Classes.Service.CarinateService import CarinateService
from Classes.Service.CockService import CockService
from Classes.Service.CoraciiformbirdService import CoraciiformbirdService
from Classes.Service.CuculiformbirdService import CuculiformbirdService
from Classes.Service.DickeybirdService import DickeybirdService
from Classes.Service.GallinaceousbirdService import GallinaceousbirdService
from Classes.Service.HenService import HenService
from Classes.Service.IberomesornisService import IberomesornisService
from Classes.Service.NesterService import NesterService
from Classes.Service.NightbirdService import NightbirdService
from Classes.Service.NonpasserinebirdService import NonpasserinebirdService
from Classes.Service.ParrotService import ParrotService
from Classes.Service.PasserineService import PasserineService
from Classes.Service.PiciformbirdService import PiciformbirdService
from Classes.Service.ProtoavisService import ProtoavisService
from Classes.Service.RatiteService import RatiteService
from Classes.Service.SinornisService import SinornisService
from Classes.Service.TrogonService import TrogonService
from Classes.Service.TwittererService import TwittererService


app = Flask(__name__)

birdRepo = BirdRepository()
birdService = BirdService(birdRepo)
apodiformbirdRepo = ApodiformbirdRepository()
apodiformbirdService = ApodiformbirdService(apodiformbirdRepo)
aquaticbirdRepo = AquaticbirdRepository()
aquaticbirdService = AquaticbirdService(aquaticbirdRepo)
archaeopteryxRepo = ArchaeopteryxRepository()
archaeopteryxService = ArchaeopteryxService(archaeopteryxRepo)
archaeornisRepo = ArchaeornisRepository()
archaeornisService = ArchaeornisService(archaeornisRepo)
birdofpassageRepo = BirdofpassageRepository()
birdofpassageService = BirdofpassageService(birdofpassageRepo)
birdofpreyRepo = BirdofpreyRepository()
birdofpreyService = BirdofpreyService(birdofpreyRepo)
caprimulgiformbirdRepo = CaprimulgiformbirdRepository()
caprimulgiformbirdService = CaprimulgiformbirdService(caprimulgiformbirdRepo)
carinateRepo = CarinateRepository()
carinateService = CarinateService(carinateRepo)
cockRepo = CockRepository()
cockService = CockService(cockRepo)
coraciiformbirdRepo = CoraciiformbirdRepository()
coraciiformbirdService = CoraciiformbirdService(coraciiformbirdRepo)
cuculiformbirdRepo = CuculiformbirdRepository()
cuculiformbirdService = CuculiformbirdService(cuculiformbirdRepo)
dickeybirdRepo = DickeybirdRepository()
dickeybirdService = DickeybirdService(dickeybirdRepo)
gallinaceousbirdRepo = GallinaceousbirdRepository()
gallinaceousbirdService = GallinaceousbirdService(gallinaceousbirdRepo)
henRepo = HenRepository()
henService = HenService(henRepo)
iberomesornisRepo = IberomesornisRepository()
iberomesornisService = IberomesornisService(iberomesornisRepo)
nesterRepo = NesterRepository()
nesterService = NesterService(nesterRepo)
nightbirdRepo = NightbirdRepository()
nightbirdService = NightbirdService(nightbirdRepo)
nonpasserinebirdRepo = NonpasserinebirdRepository()
nonpasserinebirdService = NonpasserinebirdService(nonpasserinebirdRepo)
parrotRepo = ParrotRepository()
parrotService = ParrotService(parrotRepo)
passerineRepo = PasserineRepository()
passerineService = PasserineService(passerineRepo)
piciformbirdRepo = PiciformbirdRepository()
piciformbirdService = PiciformbirdService(piciformbirdRepo)
protoavisRepo = ProtoavisRepository()
protoavisService = ProtoavisService(protoavisRepo)
ratiteRepo = RatiteRepository()
ratiteService = RatiteService(ratiteRepo)
sinornisRepo = SinornisRepository()
sinornisService = SinornisService(sinornisRepo)
trogonRepo = TrogonRepository()
trogonService = TrogonService(trogonRepo)
twittererRepo = TwittererRepository()
twittererService = TwittererService(twittererRepo)


from app import routes
