class Cofre:
    def __init__(self, titular: str, senha: str):
        self.__titular = titular
        self.__saldo = 0.0
        self.__senha = senha
        
    def depositar(self, valor):
        if valor <= 0:
            ...
        else:
            self.__saldo += valor
    
    def __verificar_senha(self, senha):
        if senha == self.__senha:
            return True
        else:
            return False
            
    def sacar(self, valor, senha):
        if self.__saldo >= valor:
            if self.__verificar_senha(senha):
                self.__saldo -= valor
            else:
                ...
        else:
            ...
        
    def consultar_saldo(self, senha):
        if self.__verificar_senha(senha):
            return self.__saldo
        return None
    
    
c = Cofre("José", "1234")
c.depositar(100)
c.sacar(30, '1234')

print(c.consultar_saldo('1234'))