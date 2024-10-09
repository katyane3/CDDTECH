arrayanotas=[0.0]*5
for x in range (5):
    arrayanotas[x] =float(input("digite as nota01:"))
media=0
for i in range (5):
    media = media + arrayanotas[i]
media= media/5
cont=0
for j in range (5):
    if arrayanotas[j]>media:
        cont=cont+1
print(cont)