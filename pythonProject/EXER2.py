arrayalunos=[""]*5
nome=(len(arrayalunos))
for i in range(5):
   arrayalunos[i]= input("digite aluno")
for x in range(nome):
  print(x,arrayalunos[x], x+1)