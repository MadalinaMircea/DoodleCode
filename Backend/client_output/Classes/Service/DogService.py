from Classes.Domain.Dog import Dog


class DogService:
    def __init__(self, repo):
        self.__repo = repo

    def add(self, description=""):
        elem = Dog(description)
        return self.__repo.add(elem)

    def delete(self, description=""):
        elem = Dog(description)
        return self.__repo.delete(elem)

    def update(self, description=""):
        elem = Dog(description)
        return self.__repo.update(elem)

    def find(self, description=""):
        elem = Dog(description)
        return self.__repo.find(elem)

    def size(self):
        return len(self.__repo)

    def get_all(self):
        return self.__repo.get_all()
