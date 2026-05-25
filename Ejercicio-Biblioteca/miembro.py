
class Miembro:
    def __init__(self, nombre, dni):
        self.__nombre = nombre
        self.__dni = dni
        self.__librosPrestados = []

    def getNombre(self):
        return self.__nombre

    def getDni(self):
        return self.__dni

    def getLibrosPrestados(self):
        return self.__librosPrestados

    def agregarLibro(self, libro):
        self.__librosPrestados.append(libro)

    def quitarLibro(self, libro):
        self.__librosPrestados.remove(libro)
