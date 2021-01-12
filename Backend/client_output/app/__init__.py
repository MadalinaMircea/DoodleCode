from flask import Flask
from Classes.Repository.DogRepository import DogRepository
from Classes.Repository.BasenjiRepository import BasenjiRepository
from Classes.Repository.CorgiRepository import CorgiRepository
from Classes.Repository.CurRepository import CurRepository
from Classes.Repository.DalmatianRepository import DalmatianRepository
from Classes.Repository.GreatpyreneesRepository import GreatpyreneesRepository
from Classes.Repository.GriffonRepository import GriffonRepository
from Classes.Repository.HuntingdogRepository import HuntingdogRepository
from Classes.Repository.LapdogRepository import LapdogRepository
from Classes.Repository.LeonbergRepository import LeonbergRepository
from Classes.Repository.MexicanhairlessRepository import MexicanhairlessRepository
from Classes.Repository.NewfoundlandRepository import NewfoundlandRepository
from Classes.Repository.PoochRepository import PoochRepository
from Classes.Repository.PoodleRepository import PoodleRepository
from Classes.Repository.PugRepository import PugRepository
from Classes.Repository.PuppyRepository import PuppyRepository
from Classes.Repository.SpitzRepository import SpitzRepository
from Classes.Repository.ToydogRepository import ToydogRepository
from Classes.Repository.WorkingdogRepository import WorkingdogRepository
from Classes.Service.DogService import DogService
from Classes.Service.BasenjiService import BasenjiService
from Classes.Service.CorgiService import CorgiService
from Classes.Service.CurService import CurService
from Classes.Service.DalmatianService import DalmatianService
from Classes.Service.GreatpyreneesService import GreatpyreneesService
from Classes.Service.GriffonService import GriffonService
from Classes.Service.HuntingdogService import HuntingdogService
from Classes.Service.LapdogService import LapdogService
from Classes.Service.LeonbergService import LeonbergService
from Classes.Service.MexicanhairlessService import MexicanhairlessService
from Classes.Service.NewfoundlandService import NewfoundlandService
from Classes.Service.PoochService import PoochService
from Classes.Service.PoodleService import PoodleService
from Classes.Service.PugService import PugService
from Classes.Service.PuppyService import PuppyService
from Classes.Service.SpitzService import SpitzService
from Classes.Service.ToydogService import ToydogService
from Classes.Service.WorkingdogService import WorkingdogService


app = Flask(__name__)

dogRepo = DogRepository()
dogService = DogService(dogRepo)
basenjiRepo = BasenjiRepository()
basenjiService = BasenjiService(basenjiRepo)
corgiRepo = CorgiRepository()
corgiService = CorgiService(corgiRepo)
curRepo = CurRepository()
curService = CurService(curRepo)
dalmatianRepo = DalmatianRepository()
dalmatianService = DalmatianService(dalmatianRepo)
greatpyreneesRepo = GreatpyreneesRepository()
greatpyreneesService = GreatpyreneesService(greatpyreneesRepo)
griffonRepo = GriffonRepository()
griffonService = GriffonService(griffonRepo)
huntingdogRepo = HuntingdogRepository()
huntingdogService = HuntingdogService(huntingdogRepo)
lapdogRepo = LapdogRepository()
lapdogService = LapdogService(lapdogRepo)
leonbergRepo = LeonbergRepository()
leonbergService = LeonbergService(leonbergRepo)
mexicanhairlessRepo = MexicanhairlessRepository()
mexicanhairlessService = MexicanhairlessService(mexicanhairlessRepo)
newfoundlandRepo = NewfoundlandRepository()
newfoundlandService = NewfoundlandService(newfoundlandRepo)
poochRepo = PoochRepository()
poochService = PoochService(poochRepo)
poodleRepo = PoodleRepository()
poodleService = PoodleService(poodleRepo)
pugRepo = PugRepository()
pugService = PugService(pugRepo)
puppyRepo = PuppyRepository()
puppyService = PuppyService(puppyRepo)
spitzRepo = SpitzRepository()
spitzService = SpitzService(spitzRepo)
toydogRepo = ToydogRepository()
toydogService = ToydogService(toydogRepo)
workingdogRepo = WorkingdogRepository()
workingdogService = WorkingdogService(workingdogRepo)


from app import routes
