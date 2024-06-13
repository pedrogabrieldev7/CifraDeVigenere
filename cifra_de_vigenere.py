from string import ascii_uppercase

alfabeto = list(ascii_uppercase)

def checando_tamanho(chave, texto):
    while len(chave) < len(texto):
        for x in range(len(chave)):
            chave += chave[x % len(chave)]
            if len(chave) == len(texto):
                break
    return chave

def validacao(chave, texto):
    if not all(char in alfabeto for char in chave) or not all(char in alfabeto for char in texto):
        print("A cifra não suporta números ou caracteres especiais, apenas letras!")
        return False
    elif len(chave) > len(texto):
        print("Chave não pode ser maior que o texto.")
        return False
    else:
        return True

def cifrando(chave, texto, alfabeto):
    texto_cifrado = ''
    for x in range(len(texto)):
        if alfabeto.index(texto[x]) + alfabeto.index(chave[x]) > 25:
            texto_cifrado += alfabeto[(alfabeto.index(chave[x]) + alfabeto.index(texto[x])) % 26]
        else:
            texto_cifrado += alfabeto[alfabeto.index(chave[x]) + alfabeto.index(texto[x])]
    return texto_cifrado

while True:
    texto = input("Digite o texto: ").replace(" ","").upper()
    chave = input("Digite uma chave: ").replace(" ","").upper()
    if validacao(chave, texto):
        print(chave, texto)
        chave = checando_tamanho(chave, texto)
        chave, texto = list(chave), list(texto)
        texto_cifrado = cifrando(chave, texto, alfabeto)
        print(f'texto criptografado: {texto_cifrado}')
        break