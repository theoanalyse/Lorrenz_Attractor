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
Tmax = 100
dt = 0.01
t = np.arange(0, Tmax, dt)

## CONDITION INITIALE
X0 = np.array([10, 10, 10])

## ON RÉSOUD LE SYSTÈME PAR ODEINT
sol = odeint(df, X0, t)
x = sol[:, 0]
y = sol[:, 1]
z = sol[:, 2]

## ON CRÉE UNE JOLIE FIGURE
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(projection="3d")

## NOMMER LES AXES
ax.set_xlabel("x")
ax.set_xlabel("y")
ax.set_xlabel("z")

## TITRE DE LA FIGURE
ax.set_title(rf"Simulating Lorrenz Attractor with $\sigma$ = {sigma}, $\beta$ = {np.round(beta, 2)}, $\rho$ = {rho}")

## ON DESSINE LE PORTRAIT DE PHASE OBTENU AVEC ODEINT ET E.E.
plt.plot(x, y, z, color="black", lw=0.2, label="ODEINT")

## ON AFFICHE TOUT :D
ax.legend()
plt.show()