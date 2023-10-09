#Melhorar o código para contemplar a situação em que o usuário não está cadastrado

D={"ana12": "1234", "lucas2019":"minhasenha","anonymous":"anonymous","root":"abc"} 

nome=input("Digite o nome de usuário:")

if (nome in D):
    senha=input("Digite a senha: ")
    if D[nome]==senha:
        print("Olá, ",nome,"!")
    else:
        print("Senha incorreta.")
else:
    print("O nome de usuário {nome} não foi encontrado".format(nome = nome))

print('-----------------')


