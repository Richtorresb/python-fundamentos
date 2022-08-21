
class Tienda:
    def __init__(self,nombre):
        self.nombre = nombre
        self.lista = []

    def agregar_producto(self, nuevo_producto):
        self.lista.append(nuevo_producto)

    def vender_producto(self, id):
        id.print_info()
        self.lista.remove(id)
        print('Removido \n')
        
    def inflación(self, porcentaje_aumento):
        for i in self.lista:
            i.actualizar_precio(porcentaje_aumento,True)

    def hacer_liquidación(self, category, porcentaje_descuento):
        for i in self.lista:
            if i.categoria == category:
                i.actualizar_precio(porcentaje_descuento,False)

    def mostrar_productos(self):
        for i in self.lista:
            i.print_info()



