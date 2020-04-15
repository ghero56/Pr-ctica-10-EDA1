posib = ["sumar","restar","multiplicar","dividir","salir"]

def switch(opcion):
    if (opcion == 1):
        print("\nSe selecciono {}".format(posib[0]))
    elif (opcion == 2):
        print("\nSe selecciono {}".format(posib[1]))
    elif (opcion == 3):
        print("\nSe selecciono {}".format(posib[2]))
    elif (opcion == 4):
        print("\nSe selecciono {}".format(posib[3]))
    elif (opcion == 5):
        print("\nSe selecciono {}".format(posib[4]))
    else:
        print("\nERROR")

switch(2)
