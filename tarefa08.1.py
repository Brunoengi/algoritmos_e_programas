def somatorioProgressaoAritmetica(valorInicial, valorFinal, Incremento):

  numeroIntervalos = (valorFinal - valorInicial)/Incremento
  somatorio = (numeroIntervalos + 1) * (valorInicial + valorFinal) / 2

  return somatorio

print("O somatório é",somatorioProgressaoAritmetica(3, 333, 3))