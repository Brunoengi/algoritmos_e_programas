nota1= float(input("Nota 1 do aluno (Entre 0 e 10): "))
nota2= float(input("Nota 2 do aluno (Entre 0 e 10): "))

media = (nota1 + nota2) / 2

if(media>= 7):
  print("O aluno foi aprovado")
else:
  print("O aluno foi reprovado")
