class CuentaBancaria:

    usuarios = []

    def __init__(self, name, tasa_interes, balance=0): 
        self.tasa_interes = tasa_interes
        self.balance = balance
        self.name = name
        CuentaBancaria.usuarios.append(self)
    
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
    
    @classmethod
    def imprimir_todas_las_instancias(cls):
        for i in cls.usuarios:
            print(f'Nombre: {i.name} - Balance: {i.balance} - Tasa de interés: {i.tasa_interes}')

richard = CuentaBancaria('richard', 0.05)
tote = CuentaBancaria('tote',0.02)



richard.deposito(200).deposito(300).deposito(500).retiro(200).generar_interés().mostrar_info_cuenta()
tote.deposito(200).deposito(800).retiro(100).retiro(100).retiro(200).retiro(100).generar_interés().mostrar_info_cuenta()

CuentaBancaria.imprimir_todas_las_instancias()