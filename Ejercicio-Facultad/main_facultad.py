
from curso import Curso
from estudiante import Estudiante


class Facultad:
    def __init__(self):
        self.__estudiantes = []
        self.__cursos = []

    def agregarEstudiante(self, estudiante):
        self.__estudiantes.append(estudiante)
        print(f"  Estudiante '{estudiante.getNombre()} {estudiante.getApellido()}' registrado (ID: {estudiante.getId()}).")

    def agregarCurso(self, curso):
        self.__cursos.append(curso)
        print(f"  Curso '{curso.getNombre()}' ({curso.getCodigo()}) registrado correctamente.")

    def buscarEstudiante(self, matricula):
        for est in self.__estudiantes:
            if est.getMatricula() == matricula:
                return est
        return None

    def buscarCurso(self, codigo):
        for curso in self.__cursos:
            if curso.getCodigo() == codigo:
                return curso
        return None

    def inscribirEstudiante(self, matricula, codigoCurso):
        estudiante = self.buscarEstudiante(matricula)
        curso = self.buscarCurso(codigoCurso)

        if estudiante is None:
            raise ValueError(f"No existe ningún estudiante con matrícula '{matricula}'.")
        if curso is None:
            raise ValueError(f"No existe ningún curso con código '{codigoCurso}'.")
        if curso.getCuposDisponibles() <= 0:
            raise PermissionError(f"El curso '{curso.getNombre()}' no tiene cupos disponibles.")

        for c in estudiante.getCursosInscriptos():
            if c.getCodigo() == codigoCurso:
                raise PermissionError(f"'{estudiante.getNombre()}' ya está inscripto en '{curso.getNombre()}'.")

        curso.agregarEstudiante(estudiante)
        estudiante.agregarCurso(curso)
        print(f"  '{estudiante.getNombre()} {estudiante.getApellido()}' inscripto en '{curso.getNombre()}' exitosamente.")

    def darBajaCurso(self, matricula, codigoCurso):
        estudiante = self.buscarEstudiante(matricula)
        curso = self.buscarCurso(codigoCurso)

        if estudiante is None:
            raise ValueError(f"No existe ningún estudiante con matrícula '{matricula}'.")
        if curso is None:
            raise ValueError(f"No existe ningún curso con código '{codigoCurso}'.")

        inscripto = any(c.getCodigo() == codigoCurso for c in estudiante.getCursosInscriptos())
        if not inscripto:
            raise PermissionError(f"'{estudiante.getNombre()}' no está inscripto en '{curso.getNombre()}'.")

        curso.quitarEstudiante(estudiante)
        estudiante.quitarCurso(curso)
        print(f"  '{estudiante.getNombre()} {estudiante.getApellido()}' dado de baja de '{curso.getNombre()}' exitosamente.")

    def mostrarCursos(self):
        if not self.__cursos:
            print("  No hay cursos registrados.")
            return
        print("\n  === ESTADO DE CURSOS ===")
        for curso in self.__cursos:
            print(f"  Curso: {curso.getNombre()} | Codigo: {curso.getCodigo()} | "
                  f"Profesor: {curso.getProfesor()} | "
                  f"Inscriptos: {curso.getCantidadInscriptos()}/{curso.getCapacidadMaxima()} | "
                  f"Cupos disponibles: {curso.getCuposDisponibles()}")
            for est in curso.getEstudiantesInscriptos():
                print(f"    -> {est.getNombre()} {est.getApellido()} (Matricula: {est.getMatricula()})")

    def mostrarEstudiantes(self):
        if not self.__estudiantes:
            print("  No hay estudiantes registrados.")
            return
        print("\n  ESTADO DE ESTUDIANTES")
        for est in self.__estudiantes:
            cursos = est.getCursosInscriptos()
            if cursos:
                nombres = ", ".join(f"'{c.getNombre()}'" for c in cursos)
                print(f"  Nombre: {est.getNombre()} {est.getApellido()} | "
                      f"Matricula: {est.getMatricula()} | Carrera: {est.getCarrera()} | "
                      f"Cursos: {nombres}")
            else:
                print(f"  Nombre: {est.getNombre()} {est.getApellido()} | "
                      f"Matricula: {est.getMatricula()} | Carrera: {est.getCarrera()} | "
                      f"Sin cursos inscriptos")



def mostrarMenu():
    print('\n')
    print('   SISTEMA DE GESTION DE FACULTAD')
    print('\n')
    print('0 - Salir')
    print('1 - Agregar estudiante')
    print('2 - Agregar curso')
    print('3 - Mostrar estudiantes')
    print('4 - Mostrar cursos')
    print('5 - Inscribir estudiante a curso')
    print('6 - Dar de baja de curso')
    print('='*20)



estudiante1 = Estudiante('Antony', 'Ruiz',   'MAT-001', 'Ingenieria en Sistemas')
estudiante2 = Estudiante('Laura',  'Gomez',  'MAT-002', 'Ingenieria en Sistemas')
estudiante3 = Estudiante('Carlos', 'Mendez', 'MAT-003', 'Licenciatura en Informatica')
curso1 = Curso('Programacion I', 'PROG1', 'Dr. Smith',  30)
curso2 = Curso('Base de Datos',  'BD01',  'Dra. Ruiz',  25)
curso3 = Curso('Redes',          'RED01', 'Ing. Torres', 2)

facultad1 = Facultad()
facultad1.agregarEstudiante(estudiante1)
facultad1.agregarEstudiante(estudiante2)
facultad1.agregarEstudiante(estudiante3)
facultad1.agregarCurso(curso1)
facultad1.agregarCurso(curso2)
facultad1.agregarCurso(curso3)

while True:
    mostrarMenu()
    opcion = input('Seleccione una opción: ')

    try:
        if opcion == '0':
            print('\n  Hasta luego!')
            break

        elif opcion == '1':
            nombre    = input('  Nombre: ').strip()
            apellido  = input('  Apellido: ').strip()
            matricula = input('  Numero de matricula: ').strip()
            carrera   = input('  Carrera: ').strip()
            if not nombre or not apellido or not matricula or not carrera:
                raise ValueError("Todos los campos son obligatorios.")
            facultad1.agregarEstudiante(Estudiante(nombre, apellido, matricula, carrera))

        elif opcion == '2':
            nombre    = input('  Nombre del curso: ').strip()
            codigo    = input('  Codigo del curso: ').strip()
            profesor  = input('  Profesor encargado: ').strip()
            cap_str   = input('  Capacidad maxima: ').strip()
            if not nombre or not codigo or not profesor or not cap_str:
                raise ValueError("Todos los campos son obligatorios.")
            if not cap_str.isdigit() or int(cap_str) <= 0:
                raise ValueError(f"La capacidad debe ser un número entero positivo (recibido: '{cap_str}').")
            facultad1.agregarCurso(Curso(nombre, codigo, profesor, int(cap_str)))

        elif opcion == '3':
            facultad1.mostrarEstudiantes()

        elif opcion == '4':
            facultad1.mostrarCursos()

        elif opcion == '5':
            matricula = input('  Matricula del estudiante: ').strip()
            codigo    = input('  Codigo del curso: ').strip()
            if not matricula or not codigo:
                raise ValueError("La matrícula y el código no pueden estar vacíos.")
            facultad1.inscribirEstudiante(matricula, codigo)

        elif opcion == '6':
            matricula = input('  Matricula del estudiante: ').strip()
            codigo    = input('  Codigo del curso: ').strip()
            if not matricula or not codigo:
                raise ValueError("La matrícula y el código no pueden estar vacíos.")
            facultad1.darBajaCurso(matricula, codigo)

        else:
            raise TypeError("Opción inválida. Ingrese un número del 0 al 6.")

    except ValueError as e:
        print(f'\n  Error de valor: {e}')
    except PermissionError as e:
        print(f'\n  Error de operación: {e}')
    except TypeError as e:
        print(f'\n  Error de tipo: {e}')
