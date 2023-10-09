a = 5
b = 10
c = a + b

print("PROGRAMA 1: A saída da aplicação referente ao valor atribuído em c é {c} O carater reservado '+' realiza uma verificação de tipo entre as variáveis 'a' e 'b', pelo fato de que ambas são do tipo number é realizada uma soma atribuida a variável 'c'. ".format(c = c))

a = 6.2
b = 4.1
c = a - b

print("PROGRAMA 2: A saída da aplicação, referente ao valor atribuído em c é {c} Nesse caso, o operador '-' realiza a verificação de tipo e consta que tanto 'a' quanto 'b' são do tipo number. Assim. ocorre um operação de subtração que é atribuida a variável c, pelo fato de que o tipo de dado é float, acontece uma descretização do número denominada ponto flutuante.".format(c = c))

a = "Modelagem "
b = "Computacional"
c = a + b

print("PROGRAMA 3: A saída da aplicação referente ao valor atribuído em c é {c}. O caracter reservado + realiza um algoritmo para a verificação de tipo, constando que tanto 'a' quanto 'b' se tratam de um tipo string, acontece a concatenação.".format(c = c))

a = []
a.append(5)
a.append(7)
a.append(11)

print("PROGRAMA 4: A saída da aplicação, referente ao vetor atribuído a variavel a será {a}. O método append realiza uma verificação sobre o comprimento do vetor, aumentando seu comprimento e inserindo no seu indice o valor fornecido como parâmetro que na primeira execução foi 5, depois 7 e depois 11".format(a = a))

a = 3
b = a > 4
c = b or True

print("PROGRAMA 5: A saída da aplicação, referente a variável c é {c}. O operador > executa um algoritmo que retorna um boolean, nesse caso como a > 4 é falso, b recebe falso. Após, é atribuido a variável c true pois o operador 'ou' resulta em verdadeiro se ao menos um dos valores de entrada for verdadeiro.".format(c = c))