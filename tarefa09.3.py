def divisores(numero):
  listaDeDivisores = []

  for n in range(numero):
    divisores = n + 1 ##Para não começar com zero
    if numero % divisores == 0:
      listaDeDivisores.append(divisores)
    
  return list(reversed(listaDeDivisores))

print(divisores(12)) ## [12, 6, 4, 3, 2, 1]
print(divisores(35)) ## [35, 7, 5, 1]
print(divisores(101)) ##Número primo [101, 1]