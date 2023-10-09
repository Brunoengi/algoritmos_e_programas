##Cria uma lista com cada palavra

resposta = []

def palavrasString(textoCompleto):
    return textoCompleto.split(' ')

def contar(textoCompleto, palavra):
    return {
        'palavra': palavra,
        'repeticoes': textoCompleto.count(palavra)
    }


def main(textoCompleto):
    palavras = palavrasString(textoCompleto)

    for palavra in palavras:
        resposta.append(contar(textoCompleto, palavra))
    return resposta

print(main('um texto um de texto de dois'))