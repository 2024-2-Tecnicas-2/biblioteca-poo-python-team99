# test_biblioteca.py
import unittest
from io import StringIO
from libro import Libro
from revista import Revista
from publicacion import Publicacion

class TestBiblioteca(unittest.TestCase):

    # Pruebas para Publicacion
    def test_constructor_publicacion(self):
        publicacion = Publicacion("El Quijote", 1605)
        self.assertEqual(publicacion.get_titulo(), "El Quijote")
        self.assertEqual(publicacion.get_anio_publicacion(), 1605)

    def test_mostrar_info_publicacion(self):
        publicacion = Publicacion("El Quijote", 1605)
        with self.assertLogs(level='INFO') as log:
            publicacion.mostrar_info()
        self.assertIn("Título: El Quijote", log.output[0])
        self.assertIn("Año de publicación: 1605", log.output[0])

    # Pruebas para Libro
    def test_constructor_libro(self):
        libro = Libro("Cien años de soledad", 1967, "Gabriel García Márquez", 417)
        self.assertEqual(libro.get_titulo(), "Cien años de soledad")
        self.assertEqual(libro.get_anio_publicacion(), 1967)
        self.assertEqual(libro.get_autor(), "Gabriel García Márquez")
        self.assertEqual(libro.get_num_paginas(), 417)

    def test_mostrar_info_libro(self):
        libro = Libro("Cien años de soledad", 1967, "Gabriel García Márquez", 417)
        with self.assertLogs(level='INFO') as log:
            libro.mostrar_info()
        self.assertIn("Título: Cien años de soledad", log.output[0])
        self.assertIn("Año de publicación: 1967", log.output[0])
        self.assertIn("Autor: Gabriel García Márquez", log.output[0])
        self.assertIn("Número de páginas: 417", log.output[0])

    # Pruebas para Revista
    def test_constructor_revista(self):
        revista = Revista("National Geographic", 2021, 150, "Exploración")
        self.assertEqual(revista.get_titulo(), "National Geographic")
        self.assertEqual(revista.get_anio_publicacion(), 2021)
        self.assertEqual(revista.get_numero_revista(), 150)
        self.assertEqual(revista.get_nombre_revista(), "Exploración")

    def test_mostrar_info_revista(self):
        revista = Revista("National Geographic", 2021, 150, "Exploración")
        with self.assertLogs(level='INFO') as log:
            revista.mostrar_info()
        self.assertIn("Título: National Geographic", log.output[0])
        self.assertIn("Año de publicación: 2021", log.output[0])
        self.assertIn("Número de la revista: 150", log.output[0])
        self.assertIn("Nombre de la revista: Exploración", log.output[0])

if __name__ == "__main__":
    unittest.main()
