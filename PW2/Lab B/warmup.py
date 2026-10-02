"""
PW2 Lab B Part 2 -- three routes to a minimum.

Compare gradient descent, Newton, and SLSQP on two functions:
  2A: f(x) = (x-3)**2 + 1          (easy, one minimum at x=3)
  2B: g(x) = x**4 - 3*x**2 + x + 5 (harder, several stationary points)
Run:  python warmup.py
"""
import numpy as np
from scipy.optimize import newton, minimize
from pytest import approx

# ---------- 2A: easy convex function ----------
def f(x):   return (x-3)**2 + 1
def df(x):  return 2*(x-3)
def d2f(x): return 2.0

# TODO 2A: minimise f three ways from x0=0 and print each result:
#   (1) gradient descent by hand (loop x = x - lr*df(x) until the step is tiny)
#   (2) scipy.optimize.newton(df, x0, fprime=d2f)
#   (3) scipy.optimize.minimize(f, x0, method="SLSQP")
x0 = 0

x_gd = x0
lr = 0.1
tol = 1e-6

print("--- Easier landscape f(x) ---\n")

while True:
  step = lr * df(x_gd)
  x_gd = x_gd - step
  if abs(step) < tol:
    break
print(f"Gradient descent: x_min = {x_gd:.6f}; y_min = {f(x_gd):.6f}")

x_min_newton = newton(df,x0, fprime=d2f)
print(f'Newton method: x_min = {x_min_newton}; y_min = {f(x_min_newton)}')

res = minimize(f, x0, method="SLSQP")
x_min_slsqp = res.x[0]
print(f"SLSQP minimize: x_min = {x_min_slsqp}; y_min = {f(x_min_slsqp)}")

# ---------- 2B: harder landscape ----------
def g(x):   return x**4 - 3*x**2 + x + 5
def dg(x):  return 4*x**3 - 6*x + 1
def d2g(x): return 12*x**2 - 6

# TODO 2B: run the same three methods on g, from x0=0 AND from x0=2.
#   For Newton (which solves dg(x)=0), also check the sign of d2g at the answer:
#   d2g > 0 means a minimum, d2g < 0 means a maximum.
#   In your README note: do the methods agree? did Newton find a minimum or
#   another stationary point? how did the starting point change the result?
x0_1 = 0
x0_2 = 2
lr = 0.01 
tol = 1e-6

x_gd_1 = x0_1
while True:
  step = lr * dg(x_gd_1)
  x_gd_1 -= step
  if abs(step) < tol:
    break

x_gd_2 = x0_2
while True:
  step = lr * dg(x_gd_2)
  x_gd_2 -= step
  if abs(step) < tol:
    break

print("\n--- Harder landscape (g(x)) ---")
print("Gradient Descent:")
print(f"  from x0=0: x = {x_gd_1:.4f}, g(x) = {g(x_gd_1):.4f}")
print(f"  from x0=2: x = {x_gd_2:.4f}, g(x) = {g(x_gd_2):.4f}")

x_newton_1 = newton(dg, x0_1, fprime=d2g)
x_newton_2 = newton(dg, x0_2, fprime=d2g)

type_1 = "minimum" if d2g(x_newton_1) > 0 else "maximum"
type_2 = "minimum" if d2g(x_newton_2) > 0 else "maximum"

print("\nNewton Method:")
print(
    f"  from x0=0: x = {x_newton_1:.4f}, g(x) = {g(x_newton_1):.4f} ({type_1},"
    f" d2g={d2g(x_newton_1):.2f})"
)
print(
    f"  from x0=2: x = {x_newton_2:.4f}, g(x) = {g(x_newton_2):.4f} ({type_2},"
    f" d2g={d2g(x_newton_2):.2f})"
)

res_1 = minimize(g, x0_1, method="SLSQP")
res_2 = minimize(g, x0_2, method="SLSQP")

print("\nSLSQP Minimize:")
print(f"  from x0=0: x = {res_1.x[0]:.4f}, g(x) = {g(res_1.x[0]):.4f}")
print(f"  from x0=2: x = {res_2.x[0]:.4f}, g(x) = {g(res_2.x[0]):.4f}")