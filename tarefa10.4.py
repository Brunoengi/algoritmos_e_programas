##Cria uma lista com cada palavra

resposta = []

def palavrasString(textoCompleto): ##Separa todas as palavras e transforma em um vetor
    return textoCompleto.split(' ')

def contar(textoCompleto, palavra): ##Conta a quantidade de palavras que tem 
    return {
        'palavra': palavra,
        'repeticoes': textoCompleto.count(palavra)
    }

def removerDuplicatas(vetor): ##Remove palavras duplicatas no vetor
    return set (vetor)

def main(textoCompleto):
    palavras = palavrasString(textoCompleto)
    palavrasSemDuplicatas = removerDuplicatas(palavras)

    for palavra in palavrasSemDuplicatas:
        resposta.append(contar(textoCompleto, palavra))
    return resposta

print(main('Esse texto tem um texto grande com um parágrafo')) ##Retorna um dicionário com as chaves 'palavra' e 'repeticoes'