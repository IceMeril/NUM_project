import numpy as np
import matplotlib.pyplot as plt
import time 
#déclaration des variables
L = 1
Tint = 0
Text = 20

#discrétisation de l'espace
N = 30
dx = L/(N-1)
dy = L/(N-1)

#Initialisation des matrices
C = np.zeros((N**2,N**2))
F = np.zeros((N**2))


def test_point_intérieur(i):
    bool = False
    if not((i+1)%N == 0 or (i+1)%N == 1): #le point n'est pas sur les lignes verticales
        if not((i+1) < N or (i+1) > int(N**2)-N): #le point n'est pas sur les lignes horizontales
            if not((i+1)%N <= 2*N/3 and (i+1)%N > N/3 and (i+1) > (N**2)/3 and (i+1) <= 2*(N**2)/3) : # le point n'est pas dans le trou du milieu
                bool = True
    return bool

#Boucle de remplissage pour l'équation de chaleur
compt = 0
for i in range(len(C)): #on parcoure chaque point de C, ligne par ligne : N**2 points au total avec N points par ligne
    if test_point_intérieur(i) :
        compt += 1
        C[i,i] = -2*((1/(dx**2))+(1/(dy**2)))
        C[i,i-1] = 1/(dx**2)
        C[i,i+1] = 1/(dx**2)
        C[i,i+N] = 1/(dy**2)
        C[i,i-N] = 1/(dy**2)
    else :
        C[i,i] = 1
print(C[N+2].reshape(N,N))
print(f"remplissage de C fait, {compt} points intérieurs trouvés")   

#Conditions aux limites 
#Sur F
for i in range (N):
    F[i] = Text #la première ligne est à la température extérieure
    F[N*i] = Text #la première colonne
    F[N*(i + 1) -1] = Text 
for i in range(N**2 - N, N**2) :
    F[i] = Text # dernière ligne

for i in range(N): #au centre, il y a un trou et la température est différente
    if i < int(2*N/3) and i >= int(N/3) : #on est dans les lignes centrales 
        for j in range(N) :
            if j%N >= int(N/3) and j%N < int(2*N/3): #colonnes centrales
                F[i*N+j] = Tint

print (F.reshape(N,N))

t_init = time.time()
#Résolution 
U = np.linalg.solve(C,F) #je pourrais faire ça de tête
t_after = time.time()
t_calc = t_after - t_init
print(f"temps de résolution du système : {t_calc} secondes")

#Résultats
plt.imshow(U.reshape(N,N), cmap='viridis', interpolation='nearest')
plt.colorbar()
plt.show()
