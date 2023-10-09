produtosEscolares = {
  'borracha': 1.00,
  'caneta': 3.00,
  'lapis': 8.50,
  'caderno': 15.30,
  'apontador': 2.50,
  'fita': 1.50,
  'mochila': 90.00,
  'grampeador': 15.00,
  'lapiseira': 5.00,
  'grafite': 2.00
}

for chave, valor in produtosEscolares.items():
  print("O produto {chave} custa {valor} real(is)".format(chave = chave, valor = valor))

print("O somatório dos itens é {somatorio} reais".format(somatorio = sum(produtosEscolares.values())))