import numpy as np 
import matplotlib.pyplot as plt 

# Initialize variables
h = []
hei = 100.0
v = []
velo = 0.0
g = 9.8
b = 0.1 
dt = 0.1
time = []

# Simulation loop
for t in np.arange(0, 10+dt, dt):
    a = g - (b * velo)
    velo += a * dt
    hei -= velo * dt

    if hei <= 0:
        break

    time.append(t)
    h.append(hei)
    v.append(velo)

# Plotting
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

ax1.plot(time, h)
ax1.set_title("Height vs Time")
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Height (m)")
ax1.grid(True)

ax2.plot(time, v)
ax2.set_title("Velocity vs Time")
ax2.set_xlabel("Time (s)")
ax2.set_ylabel("Velocity (m/s)")
ax2.grid(True)

# Terminal velocity line
v_terminal = g / b
ax2.axhline(y=v_terminal, color='r', linestyle='--', label="Terminal Velocity")
ax2.legend()

plt.tight_layout()
plt.savefig("motion_plot.pdf")
plt.show()

