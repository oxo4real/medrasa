NOTES = []
while True:
    size = int(input("Entrer le nombre des eleves : "))
    if 0 < size <= 30:
        break
for i in range(size):-g
    while(True):
        try:
            note = input(f"NOTES[{i}] = ")
            NOTES.append(float(note))
            if 0.0 <= float(note) <= 20.0:
                break
        except:
            ...
superieur = sum(1 for note in NOTES if note >= 10)
moyenne = sum(NOTES) / size
Max = max(NOTES)
Min = min(NOTES)
sup_moy = sum(1 for note in NOTES if note >= moyenne)
print("Le nombre des notes supérieurs ou égales à 10 est : ", superieur)
print("La moyenne des notes est : ", moyenne)
print("La note maximale est : ", Max)
print("La note minimale est : ", Min)
print("Le nombre des notes supérieur ou égale à la moyenne est : ", sup_moy)