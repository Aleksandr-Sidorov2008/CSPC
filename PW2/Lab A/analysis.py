"""
PW2 Lab A -- Motion from tracking data.

Read noisy free-fall position measurements, then:
  - differentiate once  -> velocity
  - differentiate twice -> acceleration (should be ~ constant -g, but noisy!)
  - integrate the acceleration back up -> recover velocity and position

Complete the TODOs. Run:  python analysis.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# TODO 1: read freefall.csv into arrays t and y
#         (hint: np.loadtxt with a comma delimiter, skipping the header)
t,y = np.loadtxt("freefall.csv", delimiter=",", skiprows=1, unpack=True)
# TODO 2: compute velocity v = derivative of y w.r.t. t   (np.gradient)
#         and acceleration a = derivative of v w.r.t. t    (np.gradient again)
#         Print the mean acceleration. Is it close to -9.81? Is it noisy?
v = np.gradient(y,t)
a = np.gradient(v,t)
print("Mean acceleration:", np.mean(a))
print("Std acceleration:", a.std())
# TODO 3: integrate a back up to recover velocity and position
#         (hint: cumulative_trapezoid(a, t, initial=0) + v[0], then again)
v_rec = cumulative_trapezoid(a, t, initial=0) + v[0]
y_rec = cumulative_trapezoid(v_rec, t, initial=0) + y[0]

max_diff = np.max(np.abs(y - y_rec))
print("Max difference in position:", max_diff)
# TODO 4: make a figure with 3 stacked panels: position, velocity, acceleration
#         vs time. Mark the true -9.81 line on the acceleration panel.
#         Save it as motion.png
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 10), sharex=True)

ax1.plot(t, y, label="Measured position")
ax1.set_ylabel("Position (m)")
ax1.grid(True)
ax1.legend()

ax2.plot(t, v, label="Velocity (gradient)")
ax2.set_ylabel("Velocity (m/s)")
ax2.grid(True)
ax2.legend()

ax3.plot(t, a, label="Acceleration (gradient)")
ax3.axhline(-9.81, color='red', linestyle='--', label="True g (-9.81 m/s²)")
ax3.set_xlabel("Time (s)")
ax3.set_ylabel("Acceleration (m/s²)")
ax3.grid(True)
ax3.legend()

plt.tight_layout()
plt.savefig("motion.png")

# BONUS : 2D Trajectory Analysis
print("\n--- Bonus Part ---")

t_2d, x_2d, y_2d = np.loadtxt("trajectory.csv", delimiter=",", skiprows=1, unpack=True)

vx = np.gradient(x_2d, t_2d)
vy = np.gradient(y_2d, t_2d)
v_total = np.sqrt(vx**2 + vy**2)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.plot(x_2d, y_2d, "b-", label="Trajectory")
ax1.set_xlabel("x (m)")
ax1.set_ylabel("y (m)")
ax1.set_title("2D Trajectory")
ax1.grid(True)
ax1.legend()

ax2.plot(t_2d, v_total, "r-", label="Total speed |v|")
ax2.set_xlabel("Time (s)")
ax2.set_ylabel("Speed (m/s)")
ax2.set_title("Speed vs Time")
ax2.grid(True)
ax2.legend()

plt.tight_layout()
plt.savefig("trajectory.png")
print("Saved trajectory.png successfully!")