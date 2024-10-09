def imprimitexto(Texto):
    tan= len(Texto)

    for w in range (tan):
        if w not in " ":
            cont+=1
        print(cont)
        t=cont(Texto)
        for p in range(t-1,-1,-1):
            print(Texto [p], end="")




