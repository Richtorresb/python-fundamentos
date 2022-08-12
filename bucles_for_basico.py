# 1. Basico.
for i in range(151):
    print(i)

# 2. Multiplos de cinco. 
for i in range(5,1001,5):
    print(i)

# 3. Contar, a la manera del Dojo.
for i in range(1,101):
    if i % 5 == 0 and i % 10 == 0:
        print('Coding Dojo')
    elif i % 5 == 0:
        print('Coding')
    else:
        print(i)

# 4. Whoa. Es un gran idiota.
suma = []
for i in range(1,500000,2):
    print(i)
    suma.append(i)
print(f'La suma total es {sum(suma)}')

# 5. Cuenta regresiva de a 4.
for i in range(2018,-1,-4):
    print(i)

# 6. Contador flexible. 
lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum,highNum+1):
    if i % mult == 0:
        print(i)

