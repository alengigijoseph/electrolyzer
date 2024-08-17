import serial
import matplotlib.pyplot as plt
import numpy as np

#serial connection with Arduino
arduino_port = "COM10"
baud_rate = 9600
ser = serial.Serial(arduino_port, baud_rate)


flow_rates = []
frequencies = []

# Reading data from Arduino and collect flow rate and frequency values
try:
    while True:
        line = ser.readline().decode().strip()
        if line.startswith("Flow rate:"):
            flow_rate = float(line.split(":")[1].split(" ")[1])
            frequency = float(line.split("Pulse frequency: ")[1].split(" ")[0])
            flow_rates.append(flow_rate)
            frequencies.append(frequency)
except KeyboardInterrupt:
    pass


ser.close()

# expected flow rates for the given frequencies
expected_flow_rates = [120, 240, 360, 480, 600, 720]
expected_frequencies = [16, 32.5, 49.3, 65.5, 82, 90.2]

# error between obtained and expected flow rates
errors = np.array(flow_rates) - np.array(expected_flow_rates)

plt.figure(figsize=(8, 6))
plt.plot(frequencies, flow_rates, 'bo-', label='Obtained Flow Rate')
plt.plot(expected_frequencies, expected_flow_rates, 'r--', label='Expected Flow Rate')

# error curve
plt.plot(frequencies, errors, 'g-', label='Error')

plt.xlabel("Pulse Frequency (Hz)")
plt.ylabel("Flow Rate (L/Hour)")
plt.title("Flow Rate and Error Curve")
plt.grid(True)
plt.legend()

plt.show()
