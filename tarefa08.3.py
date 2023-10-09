def tabuada(numero):
  if(numero >= 2 & numero <= 9):
    resposta = ""
    for x in range(10):
      resposta += "{x} x {numero} = ".format(x = x, numero = numero) + str(x * numero) + "\n"
    return resposta
  else:
    return "O número inserido não está entre 2 e 9"

print(tabuada(5))
print(tabuada(-1))