from publicacion import Publicacion

class Libro(Publicacion):
    def __init__(self, titulo, anio_publicacion, autor, num_paginas):
        super().__init__(titulo, anio_publicacion)
        self.autor = autor
        self.num_paginas = num_paginas

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Autor: {self.autor}")
        print(f"Número de páginas: {self.num_paginas}")

    def get_autor(self):
        return self.autor

    def get_num_paginas(self):
        return self.num_paginas