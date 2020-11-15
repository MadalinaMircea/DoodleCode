class ModelHelper:
    def get_info_from_image(self, image):
        return "House", ["*name: string", "+street:Shape", "-nr:int", "+move_in(name: String)",
                         "hello():int", "-hey(param1:string, param2:int)"]