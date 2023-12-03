lop = ["+", "-", "*", "/", "%", "0"]
while True:
    while True:
        op = input('Choisir un opérateur ("+", "-", "*", "/", "%") ou entrer 0 pour sortir: ')
        if op in lop:
            break
        else:
            print("l'opopérateur que vous avez choisi est invalide")
    if op == "0":
        break
    while True:
        try:
            x = float(input('entrer la valeur de x: '))
            break
        except:
            print("la valeur que vous avez enterée n'est pas un réele")
    while True:
        while True:
            try:
                y = float(input('entrer la valeur de y: '))
                break        
            except:
                print("la valeur que vous avez enterée n'est pas un réele")
        if (op != "/" and op != "%") or y != 0:
            break
        else:
            print("Math Error")
    if op =="+":
        print ("x + y = ", x + y)
    elif op =="-":
        print ("x - y = ", x - y)
    elif op =="*":
        print ("x * y = ", x * y)
    elif op =="/":
        print ("x / y = ", x / y)
    elif op =="%":
        print ("x % y = ", x % y)