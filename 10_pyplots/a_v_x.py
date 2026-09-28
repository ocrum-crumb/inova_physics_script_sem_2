import numpy as np
import matplotlib.pyplot as plt

# Define time array
t = np.linspace(0, 10, 500)  # Time from 0 to 10 seconds

# Define acceleration function (modify this as needed)
def a(t):
    return (t - np.sin(t))  # Example: a(t) = sin(t)

# Compute time step
dt = t[1] - t[0]

# Compute velocity (v) and position (x) by integrating a(t)
a_values = a(t)
v = np.concatenate(([0], np.cumsum(a_values[:-1]) * dt))  # v(t) = ∫a(t)dt
x = np.concatenate(([0], np.cumsum(v[:-1]) * dt))        # x(t) = ∫v(t)dt

# Plot the three graphs side by side
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 4))

# Plot acceleration
ax1.plot(t, a_values, label='a(t)', color='red')
ax1.set_title('Acceleration $a(t)$')
ax1.set_xlabel('Time [s]')
ax1.set_ylabel('Acceleration [m/s²]')
ax1.grid(True)

# Plot velocity
ax2.plot(t, v, label='v(t)', color='blue')
ax2.set_title('Velocity $v(t)$')
ax2.set_xlabel('Time [s]')
ax2.set_ylabel('Velocity [m/s]')
ax2.grid(True)

# Plot position
ax3.plot(t, x, label='x(t)', color='green')
ax3.set_title('Position $x(t)$')
ax3.set_xlabel('Time [s]')
ax3.set_ylabel('Position [m]')
ax3.grid(True)

plt.tight_layout()
plt.show()