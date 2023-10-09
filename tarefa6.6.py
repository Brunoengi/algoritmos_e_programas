nota1 = float(input("Nota 1 do aluno (Entre 0 e 10): "))
nota2 = float(input("Nota 2 do aluno (Entre 0 e 10): "))

mediaSemExame = (nota1 + nota2) / 2

if(mediaSemExame >= 7):
  print("O aluno foi aprovado")
else:
  print("O aluno está em exame")
  notaExame = float(input("Nota do exame (Entre 0 e 10): "))
  mediaGeral = (mediaSemExame + notaExame) / 2
  if(mediaGeral >= 5):
    print("O aluno fez o exame e está aprovado")
  else:
    print("O aluno foi reprovado")
