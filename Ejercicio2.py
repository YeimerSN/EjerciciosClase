def multiplos(lista, valor):
    for i in range(len(lista)):
        valor.append([int(x)*3 for x in str(lista[i])])
    return valor
        
print(multiplos([123,456], []))
