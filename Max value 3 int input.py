def ord_seleccion(lista):
    if (lista[0]>lista[1]):
        if (lista[0]>lista[2]):
            print ("el valor mas alto es: ", lista[0])
        else:
            print ("el valor mas alto es: ", lista[2])
    elif (lista[1]>lista[2]):
        print ("el valor mas alto es: ", lista[1])
    else:
        print ("el valor mas alto es: ", lista[2])
lista=[]
lista.append(int(input("Ingrese el primer valor de la lista : ")))
lista.append(int(input("Ingrese el segundo valor de la lista : ")))
lista.append(int(input("Ingrese el tercer valor de la lista : ")))
ord_seleccion(lista)