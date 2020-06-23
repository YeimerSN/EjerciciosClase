"""
lista corresponde a la lista para tomar el ultimo digito y valores es una lista
nula la cual guardara el ultimo elemento de cada numero en la lista
"""
def numero(lista, valores):
    for i in range(len(lista)):
        valores.append(lista[i] % 10)
    print(''.join(map(str, valores)))
            
numero([132,456,789, 000, 584, 9, 0, 5, 71871], [])
