from mascota import Mascota
from ninja import Ninja



jaimito= Mascota('Jaime','perro','Huesos')

ninja1 = Ninja('Richard', 'Torres', 'golosinas', 'pellet', jaimito)
ninja1.alimentar()
ninja1.caminar()
ninja1.bañar()
print(ninja1)

class Perro(Mascota):
    def __init__(self, name, tipo, golosinas, color):
        super().__init__(name, tipo, golosinas)
        self.color = color
    
    def __repr__(self):
        return f'{self.name}, \nTipo: {self.tipo}, \nSalud: {self.salud}, \nEnergia: {self.energia}, \nColor: {self.color}'

austin = Perro('Austin','Beagle','Calcetines','Beige')
austin.comer()
print(austin)