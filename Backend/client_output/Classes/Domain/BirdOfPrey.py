from Classes.Domain.Bird import Bird


class Birdofprey(Bird):
    """
    parameters
    """
    def __init__(self, description=""):
        self.description = description

    """
    getters and setters
    """
    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    """
    functions
    """
    
    """
    serializer
    """
    def serialize(self):
        return {"description": self.description}
