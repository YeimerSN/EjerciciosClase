class Nodo():
    def __init__(self, valor, izquierda = None, derecha = None):
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha
        
def en_orden(arbol):
    if arbol == None:
        return []
    return en_orden(arbol.izquierda) + [arbol.valor] + en_orden(arbol.derecha) 
    
arbol = Nodo(25,Nodo(15, None, Nodo(20)), Nodo(50))

print(en_orden(insertar_lista(arbol, [21,31,41,51])))

