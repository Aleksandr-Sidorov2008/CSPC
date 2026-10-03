"""
PW2 Lab B Part 5 (bonus) -- find a titration's equivalence point.

titration.csv holds a titration curve: pH versus the volume of base added.
The equivalence point is the volume where the pH changes fastest (the steep
jump). Numerically, that is where the SLOPE of the pH curve is largest.
Run:  python titration.py
"""
import numpy as np
import matplotlib.pyplot as plt

# TODO 1: read titration.csv (columns volume_base, pH) into arrays V, pH.
V,pH = np.loadtxt("titration.csv",delimiter=",",skiprows=1,unpack=True)
# TODO 2: compute the slope of the pH curve with np.gradient(pH, V), and find
#         the volume where that slope is largest (np.argmax). That is the
#         equivalence point. Print it.
dpH_dV = np.gradient(pH, V)
eq_index = np.argmax(dpH_dV)
V_eq = V[eq_index]

print(f"Equivalence point: V_eq = {V_eq:.2f} mL (pH = {pH[eq_index]:.2f})")
# TODO 3: make two plots side by side: (left) pH vs volume with a line at the
#         equivalence point; (right) the slope vs volume, showing it peaks
#         at the equivalence point. Save as titration.png.
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.plot(V, pH, color="blue", label="pH curve")
ax1.axvline(
    V_eq,
    color="red",
    linestyle=":",
    linewidth=2,
    label=f"Equivalence V_eq = {V_eq:.1f} mL",
)
ax1.set_xlabel("Volume of base (mL)")
ax1.set_ylabel("pH")
ax1.set_title("Titration Curve")
ax1.grid(True)
ax1.legend()

ax2.plot(V, dpH_dV, color="green", label="dpH/dV (Slope)")
ax2.axvline(
    V_eq,
    color="red",
    linestyle=":",
    linewidth=2,
    label=f"Peak slope at {V_eq:.1f} mL",
)
ax2.set_xlabel("Volume of base (mL)")
ax2.set_ylabel("dpH / dV")
ax2.set_title("pH Curve Derivative (Slope)")
ax2.grid(True)
ax2.legend()

plt.tight_layout()
plt.savefig("titration.png")
print("Plot saved as titration.png")