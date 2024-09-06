
from libro import Libro
from revista import Revista

def main():
    libro = Libro("Cien años de soledad", 1967, "Gabriel García Márquez", 417)
    revista = Revista("National Geographic", 2021, 150, "Exploración")

    print("Información del libro:")
    libro.mostrar_info()

    print("\nInformación de la revista:")
    revista.mostrar_info()

if __name__ == "__main__":
    main()
