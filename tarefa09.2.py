def divisivel(a, b):
  if((a % b) == 0):
    return True
  else:
    return False

print(divisivel(4, 2)) #Verdadeiro
print(divisivel(3, 3)) #Verdadeiro
print(divisivel(8, 3)) #Falso