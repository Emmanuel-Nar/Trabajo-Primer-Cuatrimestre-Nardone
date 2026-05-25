
from libro import Libro
from miembro import Miembro


class Biblioteca:
    def __init__(self):
        self.__libros = []
        self.__miembros = []

    def agregarLibros(self, libro):
        self.__libros.append(libro)
        print(f"  Libro '{libro.getTitulo()}' agregado correctamente.")

    def agregarMiembro(self, miembro):
        self.__miembros.append(miembro)
        print(f"  Miembro '{miembro.getNombre()}' registrado correctamente.")

    def buscarLibro(self, isbn):
        for libro in self.__libros:
            if libro.getIsbn() == isbn:
                return libro
        return None

    def buscarMiembro(self, dni):
        for miembro in self.__miembros:
            if miembro.getDni() == dni:
                return miembro
        return None

    def prestarLibro(self, isbn, dni):
        libro = self.buscarLibro(isbn)
        miembro = self.buscarMiembro(dni)

        if libro is None:
            raise ValueError(f"No existe ningún libro con ISBN '{isbn}'.")
        if miembro is None:
            raise ValueError(f"No existe ningún miembro con DNI '{dni}'.")
        if libro.getEstado() == "Prestado":
            raise PermissionError(f"El libro '{libro.getTitulo()}' ya está prestado.")

        libro.setEstado("Prestado")
        libro.setPrestadoA(miembro)
        miembro.agregarLibro(libro)
        print(f"  Libro '{libro.getTitulo()}' prestado a '{miembro.getNombre()}' exitosamente.")

    def devolverLibro(self, isbn, dni):
        libro = self.buscarLibro(isbn)
        miembro = self.buscarMiembro(dni)

        if libro is None:
            raise ValueError(f"No existe ningún libro con ISBN '{isbn}'.")
        if miembro is None:
            raise ValueError(f"No existe ningún miembro con DNI '{dni}'.")
        if libro.getEstado() == "Disponible":
            raise PermissionError(f"El libro '{libro.getTitulo()}' no está prestado.")
        if libro.getPrestadoA().getDni() != dni:
            raise PermissionError(f"El libro '{libro.getTitulo()}' no pertenece a '{miembro.getNombre()}'.")

        libro.setEstado("Disponible")
        libro.setPrestadoA(None)
        miembro.quitarLibro(libro)
        print(f"  Libro '{libro.getTitulo()}' devuelto por '{miembro.getNombre()}' exitosamente.")

    def mostrarLibros(self):
        if not self.__libros:
            print("  No hay libros registrados.")
            return
        print("\n  === ESTADO DE LIBROS ===")
        for libro in self.__libros:
            estado = libro.getEstado()
            if estado == "Prestado":
                estado += f" a: {libro.getPrestadoA().getNombre()} (DNI: {libro.getPrestadoA().getDni()})"
            print(f"  Título: {libro.getTitulo()} | Autor: {libro.getAutor()} | ISBN: {libro.getIsbn()} | Estado: {estado}")

    def mostrarMiembros(self):
        if not self.__miembros:
            print("  No hay miembros registrados.")
            return
        print("\n  === ESTADO DE MIEMBROS ===")
        for miembro in self.__miembros:
            libros = miembro.getLibrosPrestados()
            if libros:
                titulos = ", ".join(f"'{l.getTitulo()}'" for l in libros)
                print(f"  Nombre: {miembro.getNombre()} | Dni: {miembro.getDni()} | Libros prestados: {titulos}")
            else:
                print(f"  Nombre: {miembro.getNombre()} | Dni: {miembro.getDni()} | Sin libros prestados")




def mostrarMenu():
    print('\n' )
    print('0 - Salir')
    print('1 - Agregar libro')
    print('2 - Agregar miembro')
    print('3 - Mostrar libros')
    print('4 - Mostrar miembros')
    print('5 - Prestar libros')
    print('6 - Devolver libros')
    print('7 - Consultar estado libros')
    print('8 - Consultar estado miembros')
    print('='*18)



libro1 = Libro('Programación', 'Ema', '1234')
libro2 = Libro('Etica', 'Manu', '1235')
libro3 = Libro('DB', 'Nico', '1236')
miembro1 = Miembro('Antony', '45639678')

biblioteca1 = Biblioteca()
biblioteca1.agregarLibros(libro1)
biblioteca1.agregarLibros(libro2)
biblioteca1.agregarLibros(libro3)
biblioteca1.agregarMiembro(miembro1)

while True:
    mostrarMenu()
    opcion = input('Seleccione una opción: ')

    try:
        if opcion == '0':
            print('\n  Hasta luego!')
            break

        elif opcion == '1':
            titulo = input('  Título: ').strip()
            autor  = input('  Autor: ').strip()
            isbn   = input('  ISBN: ').strip()
            if not titulo or not autor or not isbn:
                raise ValueError("El título, autor e ISBN no pueden estar vacíos.")
            biblioteca1.agregarLibros(Libro(titulo, autor, isbn))

        elif opcion == '2':
            nombre = input('  Nombre: ').strip()
            dni    = input('  DNI: ').strip()
            if not nombre or not dni:
                raise ValueError("El nombre y el DNI no pueden estar vacíos.")
            biblioteca1.agregarMiembro(Miembro(nombre, dni))

        elif opcion == '3' or opcion == '7':
            biblioteca1.mostrarLibros()

        elif opcion == '4' or opcion == '8':
            biblioteca1.mostrarMiembros()

        elif opcion == '5':
            isbn = input('  ISBN del libro: ').strip()
            dni  = input('  DNI del miembro: ').strip()
            if not isbn or not dni:
                raise ValueError("El ISBN y el DNI no pueden estar vacíos.")
            biblioteca1.prestarLibro(isbn, dni)

        elif opcion == '6':
            isbn = input('  ISBN del libro: ').strip()
            dni  = input('  DNI del miembro: ').strip()
            if not isbn or not dni:
                raise ValueError("El ISBN y el DNI no pueden estar vacíos.")
            biblioteca1.devolverLibro(isbn, dni)

        else:
            raise TypeError("Opción inválida. Ingrese un número del 0 al 8.")

    except ValueError as e:
        print(f'\n  Error de valor: {e}')
    except PermissionError as e:
        print(f'\n  Error de operación: {e}')
    except TypeError as e:
        print(f'\n  Error de tipo: {e}')
