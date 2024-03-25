

def somar():
    print("Essa função vai somar algo.")

def mult():
    print("Essa função vai multiplicar algo.")

def findIndex(toFind, item):
    for i, valor in enumerate(toFind):
        if valor == item:
            return i
    return -1
