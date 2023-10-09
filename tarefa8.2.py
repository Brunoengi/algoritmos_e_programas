def mediaValores(vetorNumeros):

  somatorio = 0
  tamanhoVetor = len(vetorNumeros)

  if(tamanhoVetor != 10):
    return "O número de elementos inseridos não é 10, você inseriu {tamanhoVetor} elementos".format(tamanhoVetor = tamanhoVetor)
  

  for num in vetorNumeros:
    if(num >= 0 & num <=10):
      somatorio += num
    else:
      return "O valor {num}, inserido no array não está entre 0 e 10".format(num = num)
  return somatorio/tamanhoVetor

print(mediaValores([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(mediaValores([1, -1, 2, -2, 3, -3, 4, -4, 5, -5]))
print(mediaValores([1, 2, 3]))