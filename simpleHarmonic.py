import numpy as np
import matplotlib.pyplot as plt 

x = 5.0 
v = 0.0 
k = 0.2
dt = 0.1 
t = 0.0

pos = [x]
time = [t]
velo = [v]
t_m =  12.0


while t <= t_m:
    a = -k * x                # acceleration from Hooke's law
    v = v + a * dt            # Euler update for velocity
    x = x + v * dt            # Euler update for position
    t = t + dt

    time.append(t)
    velo.append(v)
    pos.append(x)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

ax1.plot(time, pos)
ax1.set_title("Height vs Time")
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Height (m)")
ax1.grid(True)

ax2.plot(time, velo)
ax2.set_title("Velocity vs Time")
ax2.set_xlabel("Time (s)")
ax2.set_ylabel("Velocity (m/s)")
ax2.grid(True)

# Terminal velocity line


plt.tight_layout()
plt.savefig("motion_plot.pdf")
