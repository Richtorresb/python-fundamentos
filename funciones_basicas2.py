
# 1. Cuenta regresiva.
from optparse import Values


arr = []
def countdown(num):
    for i in range(num,-1,-1):
        arr.append(i)
    print(arr)
    return arr

countdown(5)

# 2. Imprimir y devolver.
def imp_y_del(lis):
    print(lis[0])
    return lis[1]

lista = [1,2]
imp_y_del(lista)

# 3. Primero más longitud.
def primero_mas_longitud(arr):
    return int(arr[0]) + len(arr)

x = primero_mas_longitud([1,2,3,4,5])
print(x)

# 4. Valores mayores que el segundo.
arra = []
def valores_mayores_que_el_segundo(list2):
    for w in list2:
        if len(list2) < 2:
            return False
        if list2[1] < w:
            arra.append(w)
    print(len(arra))
    return arra

y = valores_mayores_que_el_segundo([5,2,3,2,1,4])
z = valores_mayores_que_el_segundo([3])
print(y)
print(z)

# 5. Esta longitud, ese valor.
def length_and_value(tamaño,valor):
    nueva_lista = []
    for i in range(tamaño):
        nueva_lista.append(valor)
    return nueva_lista

p = length_and_value(4,7)
h = length_and_value(6,2)
print(f'Devuelve {p} y {h}')
