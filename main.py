import numpy as np
import matplotlib.pyplot as plt

#déclaration des variables
L = 1
Tint = 1
Text = 20

#discrétisation de l'espace
N = 3
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
    F[i] = Text #la première ligne est à la température de dehors
    F[N*i] = Text #la première colonne
    F[N*(i + 1) -1] = Text 
for i in range(N**2 - N, N**2) :
    F[i] = Text # dernière ligne

for i in range(N): #au centre, il y a un trou et la température est différente
    if i < int(2*N/3) and i >= int(N/3) : #on est dans les lignes centrales 
        print('true ligne')
        for j in range(N) :
            if j%N >= int(N/3) and j%N < int(2*N/3): #colonnes centrales
                print('true colonne')
                F[i*N+j] = Tint


#Sur C
for i in range(N) :
    C[i, i] = 1
    C[N*i, N*i] = 1
    C[N*(i + 1) -1, N*(i + 1) -1] = 1

for i in range(N**2 - N, N**2) :
    C[i, i] = 1


print(C)

print(F)
#C à droite

#C au milieu

#Résolution 
#U = np.linalg.solve(C,F)


#Résultats

