# import numpy as np
# import sounddevice as sd

# # Create a sine wave
# A = 1
# f = 440
# phi = 0
# sr = 44100
# T = 2
# t = np.linspace(0, T, int(sr * T), endpoint=False)
# y = A * np.sin(2 * np.pi * f * t + phi)

# # Play the sine wave
# sd.play(y, sr)
# sd.wait()

import sounddevice as sd
import numpy as np
import time

# Initialize parameters
A = 1  # Amplitude
frequency = 1000  # Fixed frequency
phi = 0  # Phase
sr = 44100  # Sample rate

# Start the sound stream
sd_stream = sd.OutputStream(callback=None, channels=1, samplerate=sr, dtype='float32')
sd_stream.start()

# Define the time interval for changing the frequency (0.1 seconds)
change_interval = 0.1  # seconds
next_change_time = time.time() + change_interval

while True:
    # Check if it's time to change the frequency
    if time.time() >= next_change_time:
        frequency -= 10
        print(frequency)
        next_change_time += change_interval

    try:
        t = np.arange(int(sr * change_interval)) / sr  # Generate a time vector for the specified duration
        y = A * np.sin(2 * np.pi * frequency * t + phi).astype('float32')
        sd_stream.write(y)
    except KeyboardInterrupt:
        break

# Stop and close the sound stream
sd_stream.stop()
sd_stream.close()