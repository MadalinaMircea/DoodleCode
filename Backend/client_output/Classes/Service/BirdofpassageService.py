from Classes.Domain.BirdOfPassage import BirdOfPassage


class BirdOfPassageService:
    def __init__(self, repo):
        self.__repo = repo

    def add(self):
        elem = Birdofpassage()
        return self.__repo.add(elem)

    def delete(self):
        elem = Birdofpassage()
        return self.__repo.delete(elem)

    def update(self):
        elem = Birdofpassage()
        return self.__repo.update(elem)

    def find(self):
        elem = Birdofpassage()
        return self.__repo.find(elem)

    def size(self):
        return len(self.__repo)

    def get_all(self):
        return self.__repo.get_all()
