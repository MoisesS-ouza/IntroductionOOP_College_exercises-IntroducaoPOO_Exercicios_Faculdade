class Robo:
    def __init__(self, nome: str, energia: int, blindagem: int, potencia: int):
        self.nome = nome
        self.energia = energia
        self.blindagem = blindagem
        self.potencia = potencia
        
    def sofrer_ataque(self, dano):
        dano_efetivo = dano - self.blindagem
        if dano_efetivo <= 0:
            return 0
        else:
            self.energia -= dano_efetivo
            
    def atacar(self, alvo):
        return alvo.sofrer_ataque(self.potencia)
        
    def ativo(self):
        if self.energia > 0:
            return True
        else:
            return False

r1 = Robo('Alpha', 100, 3, 15)
r2 = Robo('Beta', 80, 2, 10)
r1.atacar(r2)
print(r2.energia)