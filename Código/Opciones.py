import Selectivas
import os
import time

Tiempo = ["días", "tardes", "noches"]

Hora = int(time.strftime("%H"))

nombre = input("Dime tu nombre :) \n\n-> ").title()

if(Hora < 12 and Hora < 18):
    enter = input("Buenos " + Tiempo[0] + " " + nombre + "\t(Presiona Enter)\n")
    os.system('cls')
elif(Hora >= 12 and Hora <= 18):
    enter = input("Buenas " + Tiempo[1] + " " +nombre + "\t(Presiona Enter)\n")
    os.system('cls')
else:
    enter = input("Buenas " + Tiempo[2] + " " + nombre + "\t(Presiona Enter)\n")
    os.system('cls')

op = 0

while (op != 5):
    op = int(input(
        "\t**********Calculadora**********"+"\n"
        +"1) Sumar"+"\n"
        +"2) Restar"+"\n"
        +"3) Multiplicar"+"\n"
        +"4) Dividir"+"\n"
        +"5) Salir"+"\n"
        +"\t\tOpcion-> "
    ))
    Selectivas.switch(op)

enter = input("Hasta la proxima!!!"+ "\t(Presiona Enter)\n")

os.system('cls')
