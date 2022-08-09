
#Declaración e inicializacion de variable 
num1 = 42 #numeros
num2 = 2.3 
#bolean
boolean = True
string = 'Hello World' #Strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #Lista inicializada
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #Dictionary
fruit = ('blueberry', 'strawberry', 'banana') #Tuples
print(type(fruit)) #type check #print in console
print(pizza_toppings[1]) #List- access value #print in console
pizza_toppings.append('Mushrooms') #List- add value
print(person['name']) #Dictionary- access value
person['name'] = 'George' #Dictionary- change value
person['eye_color'] = 'blue' #Dictionary- add value
print(fruit[2]) #Tuples- access value #print in console

if num1 > 45: #- conditional- if
    print("It's greater")#print in console
else: #Conditional- - else
    print("It's lower") #print in console

if len(string) < 5:
    print("It's a short word!")#print in console
elif len(string) > 15:
    print("It's a long word!") #Conditional- else if
else:
    print("Just right!")#print in console

for x in range(5): #- for loop- start in 0 and stop in 4
    print(x)
for x in range(2,5): # loop- - stop in 4
    print(x)
for x in range(2,10,3): # increment in 3
    print(x)
x = 0
while(x < 5): #- while loop- start in 0 and stop in 4
    print(x)
    x += 1 # increment in 1

pizza_toppings.pop() #- delete last value in list
pizza_toppings.pop(1) # delete second value in the list ("Sausage")

print(person)
person.pop('eye_color')
print(person) #delete value in dictionary

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue # - continue
    print('After 1st if statement') #print in console
    if topping == 'Olives':
        break

def print_hello_ten_times(): # declaration
    for num in range(10):
        print('Hello')  #print in console

print_hello_ten_times() # call function

def print_hello_x_times(x): # x is a parameter
    for num in range(x):
        print('Hello') #print in console

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello') #print in console

print_hello_x_or_ten_times() #call and print hello 10 times
print_hello_x_or_ten_times(4)  #call and print hello 4 times

"""
Bonus section
"""

# print(num3) #- NameError: name <variable name> is not defined
# num3 = 72 
# fruit[0] = 'cranberry' #TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) #KeyError: 'favorite_team'
# print(pizza_toppings[7]) # IndexError: list index out of range
#   print(boolean) #IndentationError: unexpected inden
# fruit.append('raspberry') #AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) #AttributeError: 'tuple' object has no attribute 'pop'