def detectarPositivo(lista):
    i=0
    while (i<len(lista)):
        if (lista[i]>=0):
            print ("El elemento numero ",i,"de la lista es POSITIVO")
        else:
            print ("El elemento numero ",i,"de la lista es NEGATIVO")
        i=i+1
