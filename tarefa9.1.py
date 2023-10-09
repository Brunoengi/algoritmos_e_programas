def mediaValores(vetorNumeros):

  somatorio = 0
  tamanhoVetor = len(vetorNumeros)

  for num in vetorNumeros:
      somatorio += num

  return somatorio/tamanhoVetor

print(mediaValores([1, 2, 3, 4, 5]))
print(mediaValores([0,20]))
print(mediaValores([0,20,100,200]))


