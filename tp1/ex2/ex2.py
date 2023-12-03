x = int(input("Entrer la valeur de X : "))
while True:
    y = int(input("Entrer la valeur de Y : "))
    if y == 0:
        print("Erreur : Y ne peut pas être égal à 0")
    else:
        break
print("le quotient de X / Y est: ", x // y)
print("le rest de X / y est: ", x % y)