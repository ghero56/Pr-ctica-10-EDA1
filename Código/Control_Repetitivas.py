def regresion(lim):
    i = lim
    while (True):
        i = i - 1
        print(i, end="")
        if i == 0:
            break
regresion(100)

print("\n\n")

for x in ["Perros","Gatos","Caballos","Elefantes","Gorilas"]:
    print("\n\t")
    print(x, end='')
else:
    print("\n\t")
    print("Ya no hay mas datos")



elementos = {'Helio':2, 'Neon':10, 'Argon':18, 'Kripton':36}
print("\n\n")
print("gases: \n")
for key,value in elementos.items():
    print(key," #atómico ",value)
print("\n")
print("numeros: \n")
for i in elementos.keys():
    print(i)
print("\n")
print("elementos: \n")
for i in elementos.values():
    print(i)
