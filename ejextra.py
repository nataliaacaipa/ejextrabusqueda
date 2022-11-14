#grafo = [("S", "A", 2), ("S", "B", 4), ("A", "C", 4),("A", "D", 2), ("B", "E", 4), ("B", "H", 1), ("E", "G", 2), ("H", "G", 1)]

grafo = [("S","A",3),("A","B",4),("A","C",2),("C","G",1)]

lista_nodos = []
print(lista_nodos)

mejorCamino = 100000

lista_nodos.append(("S", 0, []))
print(lista_nodos)


while len(lista_nodos)>0:

    tempNode = lista_nodos.pop()

    camino = tempNode[2].copy()
    camino.append(tempNode[0])   

    caminoTotal = tempNode[1]
    if tempNode[0] == "G":
        print("nodo encontrado")
        print("camino total:" ,caminoTotal)

        if tempNode[1]<mejorCamino:
            mejorCamino = tempNode[1]
            print("mejor camino: ", mejorCamino)
            print("nodos recorridos: ", camino)
            print("\n")
          

    for i in grafo:
            #ignora los nodos que ya, en este caso, se pase de los que la suma total del camino sea más de 6
        if i[0] == tempNode[0] and caminoTotal<mejorCamino:
            lista_nodos.append((i[1], tempNode[1]+i[2], camino))
            
    print(lista_nodos)