# 1. TAREA: imprime "Hola, mundo"
print( "Hola, mundo" )
# 2. imprime "Hola, Noelle" con el nombre en una variable
name = "Richard"
print( "Hola", name )	# con una coma
print( "Hola " + name )	# con un +
# 3. imprimir "Hola 42!" con el número en una variable
number = 10
print( "Hola", number )	# con una coma
print( "Hola " + str(number))	# con una +	-- este debería arrojar un error!
# 4. imprimir "Amo comer sushi y pizza" con las comidas en variables
fave_food1 = "hamburguesa"
fave_food2 = "pizza"
print( "Amo comer {} y {}".format(fave_food1,fave_food2) ) # con .format()
print(f'Amo comer {fave_food1} y {fave_food2}' ) # con una cadena f

