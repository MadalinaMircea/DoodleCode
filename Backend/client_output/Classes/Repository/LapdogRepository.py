from Classes.Domain.Lapdog import Lapdog


class LapdogRepository:
    def __init__(self):
        self.__elements = []

    def add(self, elem):
        if elem in self.__elements:
            return False

        self.__elements.append(elem)
        return True

    def delete(self, elem):
        if elem in self.__elements:
            self.__elements.remove(elem)
            return True
        return False

    def update(self, elem):
        index = self.find(elem)
        if not index:
            return False
        self.__elements[index] = elem

    def find(self, elem):
        index = self.__elements.index(elem)
        if index == -1:
            return False
        return index

    def get_all(self):
        return self.__elements

    def __len__(self):
        return len(self.__elements)
