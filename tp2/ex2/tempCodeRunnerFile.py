for i in range(size):
    while(True):
        try:
            element = input(f"L[{i}] = ")
            L.append(float(element))
            break
        except:
            ...