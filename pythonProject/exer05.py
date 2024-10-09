n=[0]*5
tam=len(n)
for i in range (tam):
    n[i]= int(input("leia os numeros :"))
for z in range (4,-1,-1):
    print(n[z], end= "")
