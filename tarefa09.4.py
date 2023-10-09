def divisores(numero):
  listaDeDivisores = []

  for n in range(numero):
    divisores = n + 1 ##Para não começar com zero
    if numero % divisores == 0:
      listaDeDivisores.append(divisores)
    
  listaDeDivisores = list(reversed(listaDeDivisores))
  return True if len(listaDeDivisores) == 2 else False

print(divisores(12)) ## [12, 6, 4, 3, 2, 1] -> False
print(divisores(35)) ## [35, 7, 5, 1] -> False
print(divisores(7)) ## Numero primo -> True
print(divisores(101)) ##Número primo-> True