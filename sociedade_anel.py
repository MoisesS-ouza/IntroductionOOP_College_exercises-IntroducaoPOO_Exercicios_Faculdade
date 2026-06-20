entrada = int(input())
lista_pessoas = []
hobbit = 0
humano = 0
elfo = 0
anao = 0
mago = 0
for i in range(entrada):
    pessoa = input()
    lista_pessoas.append(pessoa)
    
for elemento in lista_pessoas:
    match elemento:
        case x if ' X' in x:
            hobbit += 1
        case x if ' H' in x:
            humano += 1
        case x if ' E' in x:
            elfo += 1
        case x if ' A' in x:
            anao += 1
        case x if ' M' in x:
            mago += 1

print(f'{hobbit} Hobbit(s)')
print(f'{humano} Humano(s)')
print(f'{elfo} Elfo(s)')
print(f'{anao} Anao(oes)')
print(f'{mago} Mago(s)')
            