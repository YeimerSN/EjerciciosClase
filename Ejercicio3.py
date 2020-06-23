def sumas(lista, valor):
    for i in range(len(lista)):
        valor.append(tuple([max(lista[i]), min(lista[i]), max(lista[i]) + min(lista[i])]))
    return valor
                    
print(sumas([[1,2,3],[4,5,6],[7,8,9]], []))
