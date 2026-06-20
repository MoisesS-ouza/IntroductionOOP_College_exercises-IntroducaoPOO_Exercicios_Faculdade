class CarteiraDigital:
    def __init__(self, usuario: str, pin: str):
        self.__usuario = usuario
        self.__saldo = 0.0
        self.__pin = pin
        
    def adicionar_creditos(self, valor):
        if valor <= 0:
            ...
        else:
            self.__saldo += valor
            
    def __validar_pin(self, pin):
        if pin == self.__pin:
            return True
        else:
            return False
            
    def transferir(self, valor, pin):
        if self.__validar_pin(pin):
            if valor <= 0:
                ...
            elif valor > self.__saldo:
                ...
            else:
                self.__saldo -= valor
        else:
            ...
    
    def consultar_saldo(self, pin):
        if self.__validar_pin(pin):
            return self.__saldo
        else:
            return None
            
        
c = CarteiraDigital('Carlos', '9999')
c.adicionar_creditos(5000)
c.transferir(2000, '9999')
print(c.consultar_saldo('9999'))