import numpy as np
import matplotlib.pyplot as plt


valores=np.loadtxt("valores.txt")
x=valores[:,0]
y=valores[:,1]

analitica=np.exp(-x)

error= np.abs(((analitica-y)/analitica)*100)

plt.scatter(x,error)
plt.savefig("primerorden.png")
