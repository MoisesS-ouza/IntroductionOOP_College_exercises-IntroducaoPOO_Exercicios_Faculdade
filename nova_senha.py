dicionario = {}
dicionario['GQaku'] = 0
dicionario['ISblv'] = 1
dicionario['EOYcmw'] = 2
dicionario['FPZdnx'] = 3
dicionario['JTeoy'] = 4
dicionario['DNXfpz'] = 5
dicionario['AKUgq'] = 6
dicionario['CMWhr'] = 7
dicionario['BLVis'] = 8
dicionario['HRjt'] = 9

lista_senhas = []
quant_senhas = int(input())
for i in range(quant_senhas):
    senha = input()
    lista_senhas.append(senha)

lista_num = []

for elemento in lista_senhas:
    string_sen = ''
    for letra in elemento:
        for chave, valor in dicionario.items():
            if letra in chave:
                string_sen += str(valor)
    lista_num.append(string_sen)


for elemento in lista_num:
    quant_digitos = 0
    for digito in elemento:
        quant_digitos += 1
        if quant_digitos < 13:
            print(digito, end='')
    print()
            