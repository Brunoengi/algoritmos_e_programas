def eliminarSimbolosArgarismos(txt):
    newTxt = ''
    for letra in txt:
        
        if((letra >= 'a' and letra <= 'z') or (letra >= 'A' and letra <= 'Z')):
            newTxt += letra  
    return newTxt

print(eliminarSimbolosArgarismos('textoasdasda@#$'))