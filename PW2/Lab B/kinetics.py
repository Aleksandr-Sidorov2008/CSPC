"""
PW2 Lab B Part 3 -- fit a reaction's rate constant to measured data.

A first-order reaction decays as  C(t) = C0 * exp(-k*t).  You have noisy
concentration-vs-time measurements; find the k that best matches them.
Complete the TODOs. Run:  python kinetics.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# TODO 1: read kinetics.csv (columns time, concentration) into arrays t, C.
#         Set C0 = the first concentration.
t,C = np.loadtxt("kinetics.csv",delimiter=",",skiprows=1,unpack=True)
C0 = C[0]

# TODO 2: write total_error(k) = sum of (measured - C0*exp(-k*t))^2.
#         This is the "how bad" number: small when the model matches the data.
def total_error(k):
    global t,C,C0
    return np.sum( (C - C0*np.exp(-k*t))**2 )
# TODO 3: minimise total_error with scipy.optimize.minimize (method "SLSQP",
#         bounds [(0, 5)], start x0=0.5). Print the fitted k.
res = minimize(total_error,0.5,method="SLSQP",bounds=[(0,5)])
fitted_k = res.x[0]

print(f"Fitted k = {fitted_k:.4f}")
# TODO 4: plot the measured data (points) and your fitted curve (line) together.
#         Save as kinetics.png.
def model_concentration(C0,t,k):
    return C0*np.exp(-k*t)

t_smooth = np.linspace(t.min(), t.max(), 200)
C_smooth = model_concentration(C0, t_smooth, fitted_k)

plt.figure(figsize=(8, 5))
plt.scatter(t, C, color="red", label="Experimental data")
plt.plot(
    t_smooth,
    C_smooth,
    color="blue",
    label=f"Fitted model (k = {fitted_k:.4f})",
)
plt.xlabel("Time (s)")
plt.ylabel("Concentration (mol/L)")
plt.title("Chemical Kinetics: First-Order Reaction Fitting")
plt.grid(True)
plt.legend()
plt.savefig("kinetics.png")
print("Plot saved as kinetics.png")