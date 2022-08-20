
class Ninja:
    def __init__(self,nombre, apellido, premios, comida_mascota, mascota):
        self.nombre = nombre
        self.apellido = apellido
        self.premios = premios
        self.comida_mascota = comida_mascota
        self.mascota = mascota

    def caminar(self):
        self.mascota.jugar()

    def alimentar(self):
        self.mascota.comer()

    def bañar(self):
        self.mascota.ruido()
    
    def __repr__(self):
        return f'Name: {self.nombre}, \nApellido: {self.apellido},\nComida Mascota: {self.comida_mascota}, \nMascota: {self.mascota}'