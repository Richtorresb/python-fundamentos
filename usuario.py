class Usuario:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance_cuenta = 0
    
    def hacer_deposito(self, amount):	
        self.balance_cuenta += amount	

    def hacer_retiro(self, amount):
        self.balance_cuenta -= amount
    
    def mostrar_balance_usuario(self):
        print(f'Usuario: {self.name}, Balance: ${self.balance_cuenta}')

    def transfer_dinero(self, other_user, amount):
        self.balance_cuenta -= amount
        other_user.hacer_deposito(amount)

richard = Usuario('Richard', 'rtorresbarriga@gmail.com')
maria_jose = Usuario('Maria Jose', 'mjose.rjs@gmail.com')
tote = Usuario('Jose Ignacio', 'joseignacio@gmail.com')


richard.hacer_deposito(400)
richard.hacer_deposito(200)
richard.hacer_deposito(100)
richard.hacer_retiro(50)
richard.mostrar_balance_usuario()

maria_jose.hacer_deposito(500)
maria_jose.hacer_deposito(500)
maria_jose.hacer_retiro(250)
maria_jose.hacer_retiro(150)
maria_jose.mostrar_balance_usuario()

tote.hacer_deposito(1000)
tote.hacer_retiro(100)
tote.hacer_retiro(200)
tote.hacer_retiro(300)
tote.mostrar_balance_usuario()

richard.transfer_dinero(tote, 100)
richard.mostrar_balance_usuario()
tote.mostrar_balance_usuario()