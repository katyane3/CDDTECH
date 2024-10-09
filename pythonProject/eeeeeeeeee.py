arraynomes=[""]*5
arraysenhas=[""]*5
tam=len(arraysenhas)
for z in range (tam):
    arraynomes[z]=input("digite um nome:")
    arraysenhas[z]=int(input(" digite a senha:"))
for x in range(tam):

 print(f" usuario {arraynomes[x]} tem a senha {arraysenhas[x]}"
       f"\n e sua posição é {x}")
    