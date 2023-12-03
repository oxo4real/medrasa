L=[12,13,-4,41,88,700]
taille=len(L)
for i in range(0,taille):
 print("L[",i,"]=\t", L[i])
L.reverse() # inverser la liste
for i in range(0,taille):
 print("L[",i,"]=\t", L[i])
L.sort() # trier les element de la liste
for i in range(0,taille):
 print("L[",i,"]=\t", L[i])