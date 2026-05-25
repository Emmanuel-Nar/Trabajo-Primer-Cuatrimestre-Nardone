
class Curso:
    def __init__(self, nombre, codigo, profesor, capacidadMaxima):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__profesor = profesor
        self.__capacidadMaxima = capacidadMaxima
        self.__estudiantesInscriptos = []

    def getNombre(self):
        return self.__nombre

    def getCodigo(self):
        return self.__codigo

    def getProfesor(self):
        return self.__profesor

    def getCapacidadMaxima(self):
        return self.__capacidadMaxima

    def getCantidadInscriptos(self):
        return len(self.__estudiantesInscriptos)

    def getCuposDisponibles(self):
        return self.__capacidadMaxima - len(self.__estudiantesInscriptos)

    def getEstudiantesInscriptos(self):
        return self.__estudiantesInscriptos

    def agregarEstudiante(self, estudiante):
        self.__estudiantesInscriptos.append(estudiante)

    def quitarEstudiante(self, estudiante):
        self.__estudiantesInscriptos.remove(estudiante)
