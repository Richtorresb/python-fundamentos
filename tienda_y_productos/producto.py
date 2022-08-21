class Producto:
    def __init__(self,nombre,precio,categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def actualizar_precio(self,cambio_porcentaje,esta_elevado=True):
        if esta_elevado == True:
            self.precio *= (1+cambio_porcentaje)
        else:
            self.precio *= (1 - cambio_porcentaje)
    
    def print_info(self):
        print(f'Nombre producto: {self.nombre},Categoría: {self.categoria}, Precio: {self.precio}')