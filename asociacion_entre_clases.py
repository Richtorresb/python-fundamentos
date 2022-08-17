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
        self.cuenta = {}

    def crear_cuenta(self,nombre_cuenta,tasa_interes):
        self.cuenta[nombre_cuenta] = CuentaBancaria(tasa_interes)
        print(f'Cuenta nueva: {nombre_cuenta}, Tasa de interes: {tasa_interes}')
        return self

    def hacer_deposito(self,nombre_cuenta,amount):
        self.cuenta[nombre_cuenta].deposito(amount)
        print(f'Deposito por : {amount}, en Cuenta :{nombre_cuenta}')
        return self

    def retiro(self,nombre_cuenta, amount):
        self.cuenta[nombre_cuenta].retiro(amount)
        print(f'Retiro por: {amount}, Cuenta: {nombre_cuenta}')
        return self
    
    def transferencia_interna(self,nombre_cuenta,nombre_a_transferir,amount):
        self.cuenta[nombre_cuenta].retiro(amount)
        if self.cuenta[nombre_cuenta].balance >= 0:
            self.cuenta[nombre_a_transferir].deposito(amount)
            print(f'Transferencia realizada a {nombre_a_transferir} por {amount}')

    def mostrar_balance_usuario(self,nombre_cuenta):
        print(f'User: {self.name}, Email: {self.email}')
        self.cuenta[nombre_cuenta].mostrar_info_cuenta()
        return self
    
    def generar_interes(self,nombre_cuenta):
        self.cuenta[nombre_cuenta].generar_interés()
        print(f'Generando interés')
        return self

richard = Usuario('Richard Torres','rtorresbarriga@gmail.com')
richard.crear_cuenta('bank1',0.2)
richard.hacer_deposito('bank1',1000)
richard.retiro('bank1',200)
richard.crear_cuenta('bank2',0.5)
richard.hacer_deposito('bank2',2000)


richard.transferencia_interna('bank1','bank2',200)
richard.mostrar_balance_usuario('bank1')
richard.mostrar_balance_usuario('bank2')




