import numpy as np
import matplotlib.pyplot as plt

#déclaration des variables
L = 1
Tint = 0
Text = 20

#discrétisation de l'espace
N = 200
dx = L/N
dy = L/N
X = np.linspace(0, L, N)
Y = np.linspace(0, L, N)

#Initialisation de C
C = np.zeros(N,N)
F = np.zeros(N)

#Boucle de remplissage



#Conditions aux limites

#Pour F

#Pour C à gauche

#C à droite

#C au milieu

#Résolution 



#Résultats