# Math
import math

x = math.cos(math.pi)

print("\n\a\t",x)
print("\n")
print(dir(math))
print("\n")
En=input("Presiona Enter Para Graficar")

# Matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10,0.1)

y = np.sin(x)

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y = xcos(x)')
plt.title('Puntos')
plt.show()
