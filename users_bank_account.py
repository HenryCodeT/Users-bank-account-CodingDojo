class CuentaBancaria:
    cuentas = []
    def __init__(self, tasa_interes, balance): 
        self.tasa_interes = tasa_interes
        self.balance= balance
        CuentaBancaria.cuentas.append(self)

    def deposito(self, amount):
        self.balance += amount
        return self

    def retiro(self, amount):
        self.balance -= amount
        return self

    def mostrar_info_cuenta(self):
        print('balance: $%d'%(self.balance))
        return self

    def generar_interes(self):
        if self.balance > 0:
            self.balance += (self.balance * self.tasa_interes)
        return self
    @classmethod
    def imprimir_todas_cuentas(cls):
        for cuenta in cls.cuentas:
            cuenta.mostrar_info_cuenta()

class User:
    def  __init__ ( self , name, email):
        self.name = name
        self.email = email
        self.cuenta  =  CuentaBancaria(tasa_interes = 0.02 , balance = 0 )
    
    def hacer_deposito(self, amount):
        self.cuenta.deposito(amount)
        return self
    
    def hacer_retiro(self,amount):
        self.cuenta.retiro(amount)
        return self
    
    def mostrar_balance_usuario(self):
        print('balance: $%d'%(self.cuenta.balance))
        return self