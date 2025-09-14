import numpy as np 
import matplotlib.pyplot as plt 

g = 9.81 
l = 1.0 
m = 1.0

dt = 0.001 
tm = 20.0
n = int(tm / dt)

t = np.linspace(0, tm, n+1)
theta = np.zeros(n + 1)
omega = np.zeros(n + 1)
theta1 = np.zeros(n + 1)
omega1 = np.zeros(n + 1)
energy = np.zeros(n + 1)
energy1 = np.zeros(n + 1)

theta[0] = np.pi / 2.0 
omega[0] = 0.0
theta1[0] = np.pi / 2.0 
omega1[0] = 0.0 

for i in range(n):
    a = -(g / l) * np.sin(theta[i])

    omega[i + 1] = omega[i] + dt * a
    theta[i + 1] = theta[i] + dt * omega[i+1]

# --- 5. Calculate energy at each step ---
K = 0.5 * m * (l * omega)**2
U = m * g * l * (1 - np.cos(theta))
energy = K + U

#------------------------------------
#Standart Euler Method
#------------------------------------
for i in range(n):
    a1 = -(g / l) * np.sin(theta1[i])
    
    omega1[i + 1] = omega1[i] + dt * a1
    theta1[i + 1] = theta1[i] + dt * omega1[i]

K1 = 0.5 * m * (l * omega1)**2
U1 = m * g * l * (1 - np.cos(theta1))
energy1 = K1 + U1

# --- 6. Visualize the results ---
fig, ax = plt.subplots(2, 2, figsize=(12, 5))
ax[0, 0].plot(t, energy1, label='Total Energy(Standart Euler)')
ax[0,0].set_title('Energy Conservation (Euler-Standart)')
ax[0,0].set_xlabel('Time (s)')
ax[0,0].set_ylabel('Total Energy(Joules)')
ax[0,0].grid(True)
ax[0,0].set_ylim(bottom=energy[0]*0.9, top=energy1[0]*1.1) 
#ax[0].legend(True)
ax[0,1].plot(t, energy, label='Total Energy')
ax[0,1].set_title('Energy Conservation')
ax[0,1].set_xlabel('Time (s)')
ax[0,1].set_ylabel('Total Energy (Joules)')
ax[0,1].set_ylim(bottom=energy[0]*0.9, top=energy[0]*1.1) # Zoom in on y-axis
ax[0,1].grid(True)
#ax[1].legend()

ax[1,1].plot(np.degrees(omega),np.degrees(theta) , label='Phase Diagram')
ax[1,1].set_title('Phase Diagram Euler-Cromer')
ax[1,1].set_xlabel('omega')
ax[1,1].set_ylabel('Theta')
ax[1,1].grid(True)

ax[1,0].plot(np.degrees(omega1),np.degrees(theta1) , label='Phase Diagram')
ax[1,0].set_title('Phase Diagram Euler-Standart')
ax[1,0].set_xlabel('omega')
ax[1,0].set_ylabel('Theta')
ax[1,0].grid(True)
plt.tight_layout()
plt.show()


