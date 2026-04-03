import numpy as np
import matplotlib.pyplot as plt

#déclaration des variables
L = 1
Tint = 0
Text = 20

#discrétisation de l'espace
N = 9
dx = L/N
dy = L/N
X = np.linspace(0, L, N)
Y = np.linspace(0, L, N)

#Initialisation de C
C = np.zeros((N**2,N**2))
F = np.zeros((N**2))

#Boucle de remplissage



#Conditions aux limites 
#Sur F
for i in range (N):
    F[i] = Text
    F[N*i] = Text
    F[N*(i + 1) -1] = Text
for i in range(N**2 - N, N**2) :
    F[i] = Text

#Sur C
for i in range(N) :
    C[i, i] = 1
    C[N*i, N*i] = 1
    C[N*(i + 1) -1, N*(i + 1) -1] = 1

for i in range(N**2 - N, N**2) :
    C[i, i] = 1



print(C)
#C à droite

#C au milieu

#Résolution 



#Résultats