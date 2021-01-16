from Classes.Domain.Parrot import Parrot


class ParrotService:
    def __init__(self, repo):
        self.__repo = repo

    def add(self):
        elem = Parrot()
        return self.__repo.add(elem)

    def delete(self):
        elem = Parrot()
        return self.__repo.delete(elem)

    def update(self):
        elem = Parrot()
        return self.__repo.update(elem)

    def find(self):
        elem = Parrot()
        return self.__repo.find(elem)

    def size(self):
        return len(self.__repo)

    def get_all(self):
        return self.__repo.get_all()
