import numpy as np 
import matplotlib.pyplot as plt 

g = 10 
l = 1.0 

q = 0.5

dt = 0.01 
t_max = 20.0
n = int(t_max / dt)

t = np.linspace(0, t_max, n+1)
theta = np.zeros(n + 1)
omega = np.zeros(n + 1)

theta[0] = np.pi / 2.0 
omega[0] = 0.0 

for i in range(n):
    dtheta_dt = omega[i]
    domega_dt = -(g / l ) * np.sin(theta[i]) - q*omega[i]

    #Euler update rules 
    theta[i+1] = theta[i] + dt * dtheta_dt
    omega[i+1] = omega[i] + dt * domega_dt

fig, ax = plt.subplots(1, 2, figsize=(6.0, 3.71))
ax[0].plot(t, np.degrees(theta), label = 'Pendulum Angle (Euler Method)')
#plt.title('Simulation of a Simple Pendulum')
#plt.xlabel('Time(s)')
#plt.ylabel('Angle(degrees)')
ax[1].plot(np.degrees(theta), np.degrees(omega))

plt.grid(True)
plt.legend()
plt.show()
