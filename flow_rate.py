
import matplotlib.pyplot as plt
import numpy as np


flow_rates = []
pulse_frequencies = [16, 32.5,49.3,65.5,82,90.2]
expected_flow_rates = [120, 240, 360, 480, 600, 720]  # Expected flow rates corresponding to pulse frequencies
obtained_flow_rate =[121.5,99,22.5,45,67.5,31.5]
obtained_frequencies=[27,22,5,1,15,7]


errors = np.array(expected_flow_rates) - np.array(obtained_flow_rate)
plt.subplot(2, 1, 2)
plt.plot(pulse_frequencies, errors, 'ro-', label='Error')
plt.xlabel("Pulse Frequency (Hz)")
plt.ylabel("Error (L/Hour)")
plt.title("Error Curve")
plt.grid(True)
plt.legend()

plt.tight_layout()

plt.show()
