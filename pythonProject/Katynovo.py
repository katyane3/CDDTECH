from NEWKATY import imprime


def imprimeVogais(vogais):
    cont=0
    t=len(vogais)
    for k in range (t):
        if vogais[k] in "aeiouAEIOU":
            cont+=1

            print(f"encontramos {cont} vogais")

def imprimeSoma(*numeros):
    soma= sun(numeros)
    print(imprimeSoma)

def imprimeLista(lista):
    novalista=[]
    for c in lista:
        if c not in novalista:
            novalista.append(c)
        print(novalista)



def imprimeprimo(numeros):
    if (numeros ==1):
        return numeros(f" não é primo")
    elif(numeros==2):
        return numeros(f" é primo")
    else:
        for x in range(2, numeros):
            if(n% x==0):
                return numeros(f" não é primo")
    return numeros(f" são primos")

