L=[]
size = 15
for i in range(size):
    while(True):
        try:
            element = input(f"L[{i}] = ")
            L.append(float(element))
            break
        except:
            print("Erreur")
somme = 0
for i in range(size):
    somme += L[i]
moyenne = somme / size
superieur = 0
for i in range(size):
    if L[i] > moyenne :
        superieur += 1
positves = 0
for i in range(size):
    if L[i] > 0 :
        positves += 1
pair = 0
for i in range(size):
    if L[i] % 2 == 0 :
        pair += 1
print("la somme est : ", somme)
print("la moyenne est : ", moyenne)
print("le nombre des nombres superieur a la moyenne est : ", superieur)
print("le nombre des nombres positves est : ", positves)
print("le nombre des nombres pair est : ", pair)