import numpy as np
import matplotlib.pyplot as plt

# Generate position data for the detector screen
x = np.linspace(-5, 5, 1000)

# Simulate interference pattern without observer
no_observer = 100 * np.cos(x)**2

# Simulate interference pattern with observer (perturbed)
with_observer = 80 * np.cos(x)**2 + 20

# Plot results
plt.plot(x, no_observer, label='No Observer')
plt.plot(x, with_observer, '--', label='With Observer')
plt.xlabel('Position on Detector Screen (mm)')
plt.ylabel('Photon Count')
plt.legend()
plt.grid(True)
plt.show()
