class Usuario:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance_cuenta = 0
    
    def hacer_deposito(self, amount):	
        self.balance_cuenta += amount	
        return self

    def hacer_retiro(self, amount):
        self.balance_cuenta -= amount
        return self
    
    def mostrar_balance_usuario(self):
        print(f'Usuario: {self.name}, Balance: ${self.balance_cuenta}')
        return self

    def transfer_dinero(self, other_user, amount):
        self.balance_cuenta -= amount
        other_user.hacer_deposito(amount)
        return self

richard = Usuario('Richard', 'rtorresbarriga@gmail.com')
maria_jose = Usuario('Maria Jose', 'mjose.rjs@gmail.com')
tote = Usuario('Jose Ignacio', 'joseignacio@gmail.com')


richard.hacer_deposito(400).hacer_deposito(200).hacer_deposito(200).hacer_retiro(50).mostrar_balance_usuario()

maria_jose.hacer_deposito(500).hacer_deposito(500).hacer_retiro(250).hacer_retiro(150).mostrar_balance_usuario()

tote.hacer_deposito(1000).hacer_retiro(100).hacer_retiro(200).hacer_retiro(300).mostrar_balance_usuario()

richard.transfer_dinero(tote, 100).mostrar_balance_usuario()
tote.mostrar_balance_usuario()