
def collatz(num: int):
    if num % 2 == 0:
        resul = num / 2
    else:
        resul = 3 * num + 1
    print(resul)
    collatz(resul)


numero: int = int(input("Ingrese un numero: "))
collatz(numero)
