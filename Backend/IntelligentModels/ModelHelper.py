# from IntelligentModels.DoodleRecognition.DoodleModel import DoodleModel


class ModelHelper:
    def __init__(self):
        # self.model = DoodleModel(False)
        pass

    def get_info_from_image(self, image, pars_and_funcs):
        if pars_and_funcs == "":
            pars = []
        else:
            pars = pars_and_funcs.split('\n')
        # return self.model.predict(image), pars
        return "House", ["*name: string", "+street:Shape", "-nr:int", "+move_in(name: String)",
                         "hello():int", "-hey(param1:string, param2:int)"]
