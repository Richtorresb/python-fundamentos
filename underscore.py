class Underscore:
    def map(self, iterable, callback):
        new_list = []
        for i in iterable:
            new_list.append(callback(i))
        print(new_list)
        return new_list

    def find(self, iterable, callback):
        for i in iterable:
            if callback(i) == True:
                print(i)
                return i

    def filter(self, iterable, callback):
        new_list = []
        for i in iterable:
            if callback(i) == True:
                new_list.append(i)
        print(new_list)
        return new_list
    def reject(self, iterable, callback):
        new_list = []
        for i in iterable:
            if callback(i) == False:
                new_list.append(i)
        print(new_list)

# acabas de crear una biblioteca con 4 métodos!

# creemos una instancia de nuestra clase
_ = Underscore() 
_.map([1,2,3], lambda x: x*2) # debería devolver [2,4,6]
_.find([1,2,3,4,5,6], lambda x: x>4) # debería devolver el primer valor que sea mayor que 4
_.filter([1,2,3,4,5,6], lambda x: x%2==0) # debería devolver [2,4,6]
_.reject([1,2,3,4,5,6], lambda x: x%2==0) # debería devolver [1,3,5]

