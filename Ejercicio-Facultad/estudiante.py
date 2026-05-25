

import uuid

class Estudiante:
    def __init__(self, nombre, apellido, matricula, carrera):
        self.__id = str(uuid.uuid4())[:8].upper()
        self.__nombre = nombre
        self.__apellido = apellido
        self.__matricula = matricula
        self.__carrera = carrera
        self.__cursosInscriptos = []

    def getId(self):
        return self.__id

    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

    def getMatricula(self):
        return self.__matricula

    def getCarrera(self):
        return self.__carrera

    def getCursosInscriptos(self):
        return self.__cursosInscriptos

    def agregarCurso(self, curso):
        self.__cursosInscriptos.append(curso)

    def quitarCurso(self, curso):
        self.__cursosInscriptos.remove(curso)
