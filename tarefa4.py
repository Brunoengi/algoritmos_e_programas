def recalcularSalario(salarioAnterior: float, percentualReajuste: int): 
  return salarioAnterior * (1 + percentualReajuste/100)

print(recalcularSalario(1200, 10)) #Salário anterior de 1200 e 10% de reajuste, saída 1320
print(recalcularSalario(2000, 50)) #Salário anterior de 2000 e 50% de reajuste, saída 3000

import datetime

def calcularIdade(anoNascimento: int):
  anoAtual = datetime.datetime.now().year
  return anoAtual - anoNascimento

print(calcularIdade(1980)) 
print(calcularIdade(2000))
print(calcularIdade(2002))