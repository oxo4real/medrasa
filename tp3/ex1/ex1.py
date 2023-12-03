while True:
    name = input("Entrer votre nom: ")
    if name[0].isupper():
        print(f"Bonjour '{name}'!")
        break
    else:
        print("erreur, le premier caractère doit être en majuscule")