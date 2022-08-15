class CuentaBancaria:

    def __init__(self, tasa_interes, balance=0): 
        self.tasa_interes = tasa_interes
        self.balance = balance
    
    def deposito(self, amount):
        self.balance += amount
        return self

    def retiro(self, amount):
        if (self.balance - amount) < 0:
            print("Fondos insuficientes: cobrando una tarifa de $5")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
    
    def mostrar_info_cuenta(self):
        print(f'Balance:${self.balance} y la tasa de interes es: {self.tasa_interes}')
        return self
    
    def generar_interés(self):
        if self.balance > 0:
            self.balance *= ( 1 + self.tasa_interes)
        return self

class Usuario:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cuenta = CuentaBancaria(0.02, balance=0)	

    def hacer_deposito(self,amount):
        self.cuenta.deposito(amount)
        return self

    def retiro(self, amount):
        self.cuenta.retiro(amount)
        return self
    
    def transferencia(self,user,amount):
        self.cuenta.retiro(amount)
        if self.cuenta.balance >= 0:
            user.hacer_deposito(amount)

    
    def mostrar_balance_usuario(self):
        print(f'User: {self.name}, Email: {self.email}')
        self.cuenta.mostrar_info_cuenta()
        return self
    
    def generar_interes(self):
        self.cuenta.generar_interés()
        return self

richard = Usuario('Richard Torres','rtorresbarriga@gmail.com')
tote = Usuario('tote', 'tote@gmail.com')

richard.hacer_deposito(500)
richard.transferencia(tote,100)
richard.mostrar_balance_usuario()
tote.mostrar_balance_usuario()



