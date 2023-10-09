idade = int(input("Qual a sua idade?"))

if (idade < 0):
  print("Erro: digite uma idade válida")
elif(idade < 18):
  print("Você ainda não pode dirigir")  
else:
  print("Você já pode dirigir")