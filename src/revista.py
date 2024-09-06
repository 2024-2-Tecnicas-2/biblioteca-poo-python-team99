from publicacion import Publicacion

class Revista(Publicacion):
    def __init__(self, titulo, anio_publicacion, numero_revista, nombre_revista):
        super().__init__(titulo, anio_publicacion)
        self.numero_revista = numero_revista
        self.nombre_revista = nombre_revista

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de la revista: {self.numero_revista}")
        print(f"Nombre de la revista: {self.nombre_revista}")

    def get_numero_revista(self):
        return self.numero_revista

    def get_nombre_revista(self):
        return self.nombre_revista