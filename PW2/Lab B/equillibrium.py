"""
PW2 Lab B Part 4 -- chemical equilibrium via the equilibrium constant K.

Reaction  H2 + I2 <=> 2 HI, starting from 1 mol H2 and 1 mol I2.
As the reaction proceeds by an extent x:  H2 = 1-x,  I2 = 1-x,  HI = 2x.
At equilibrium the composition satisfies the equilibrium constant
        K = [HI]^2 / ([H2][I2]) = (2x)^2 / ((1-x)(1-x)).
Given K, find the extent x. Solve it TWO ways and compare.
Run:  python equilibrium.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 15.6
a = b = 1.0

# TODO 1: write k_imbalance(x) = (2x)^2/((a-x)(b-x)) - K.
#         It equals zero exactly at equilibrium.
def k_imbalance(x):
    global a,b,K
    return (2*x)**2/((a-x)*(b-x)) - K
# TODO 2 (method 1): use scipy.optimize.newton to find the root of k_imbalance
#         (start x0=0.5). This is root-finding.
x_newton = newton(k_imbalance, x0=0.5)
# TODO 3 (method 2): use scipy.optimize.minimize to minimise k_imbalance(x)**2
#         (method "SLSQP", bounds [(0, 0.999)], x0=[0.5]). Print both answers
#         and confirm they agree.
def objective(x):
  return k_imbalance(x[0]) ** 2

res = minimize(objective, x0=[0.5], bounds=[(0, 0.999)], method="SLSQP")
x_minimized = res.x[0]

print(f"Newton method:   x = {x_newton:.4f}")
print(f"Minimize method: x = {x_minimized:.4f}")
# TODO 4: report the equilibrium amounts (H2, I2, HI), and plot how the three
#         amounts change with the extent x, marking the equilibrium. Save
#         equilibrium.png.
x_eq = x_newton
n_H2_eq = a - x_eq
n_I2_eq = b - x_eq
n_HI_eq = 2 * x_eq

print("\nEquilibrium Composition:")
print(f"  nH2 = {n_H2_eq:.4f} mol")
print(f"  nI2 = {n_I2_eq:.4f} mol")
print(f"  nHI = {n_HI_eq:.4f} mol")

x_smooth = np.linspace(0, 0.99, 200)
H2 = a - x_smooth
I2 = b - x_smooth
HI = 2 * x_smooth

plt.figure(figsize=(8, 5))
plt.plot(x_smooth, H2, label="H2 (1 - x)", color="blue")
plt.plot(x_smooth, I2, label="I2 (1 - x)", color="green", linestyle="--")
plt.plot(x_smooth, HI, label="HI (2x)", color="orange")

plt.axvline(
    x_eq,
    color="red",
    linestyle=":",
    linewidth=2,
    label=f"Equilibrium (x = {x_eq:.4f})",
)

plt.xlabel("Reaction Extent (x)")
plt.ylabel("Amount (mol)")
plt.title("Chemical Equilibrium: H2 + I2 <=> 2 HI")
plt.grid(True)
plt.legend()
plt.savefig("equilibrium.png")
print("\nPlot saved as equilibrium.png")