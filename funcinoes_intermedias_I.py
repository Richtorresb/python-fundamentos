# 1. Actualizar valores en diccionarios y listas.

x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
    # Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
x[1][0] = 15 
    #Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
estudiantes[0]['last_name'] = 'Bryant'
    #En el directorio_deportes, cambia "Messi" por "Andrés".
directorio_deportes['fútbol'][0] = 'Andrés'
    #Cambia el valor 20 en z a 30.
z[0]['y'] = 30


#2. Iterar a través de una lista de diccionarios
def iterateDictionary(some_list):
    for x in some_list:
            for y,w in x.items():
                print(f'{y} - {w}')
        
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(estudiantes) 


# 3. Obtener valores de una lista de diccionarios
def iterateDictionary2(key_name, some_list):
    for i in some_list:
        print(i[key_name])

estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

iterateDictionary2('first_name',estudiantes)
iterateDictionary2('last_name',estudiantes)

# 4. Iterar a través de un diccionarios con valores de lista
def printInfo(some_dict):
    for i in some_dict:
        print(f'\n{len(some_dict[i])} {i.upper()}')
        for x in some_dict[i]:
            print(x)
            
        
dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)


