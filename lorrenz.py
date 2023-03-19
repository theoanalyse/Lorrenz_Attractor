## PAQUETS
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

## PARAMÈTRES
sigma = 10
rho = 28
beta = 8/3

## EQUATIONS DU MODÈLE
def df(X, t):
    x, y, z = X[0], X[1], X[2] # on récup les coords 1-par-1
    dx = sigma*(y - x) # dx/dt
    dy = rho*x -y -x*z # dy/dt
    dz = x*y -beta*z # dz/dt
    return np.array([dx, dy, dz]) # on retourne le vecteur X + dt*dF


## MAILLAGE EN TEMPS
t = np.linspace(0, 100, 10001)

## CONDITION INITIALE
X0 = np.array([10, 10, 10])

## ON RÉSOUD LE SYSTÈME
sol = odeint(df, X0, t)
x = sol[:, 0]
y = sol[:, 1]
z = sol[:, 2]

## ON CRÉE UNE JOLIE FIGURE
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(projection="3d")

## ON DESSINE LE PORTRAIT DE PHASE
plt.plot(x, y, z, color="black", lw=0.5)

## ON AFFICHE TOUT :D
plt.show()