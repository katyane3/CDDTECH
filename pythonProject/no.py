num=[1,2,3,4,5,-6,7,8,9]
maior=0
menor=1
for k in num:
    if  k%2==0:
     print(k, end= "")
for z in num:
    if z > maior:
        maior=z
    if z < menor:
        menor=z

maior=max(num)
menor=min(num)
print()
print(maior)