from tienda import Tienda
from producto import Producto



if __name__=='__main__':
    supermercado = Tienda('lider')
    manzana = Producto('manzana',500,'frutas')
    pera = Producto('pera',300,'frutas')
    bebida = Producto('bebida',1000,'bebestible')

    supermercado.agregar_producto(manzana)
    supermercado.agregar_producto(pera)
    supermercado.agregar_producto(bebida)

    
    supermercado.mostrar_productos()

