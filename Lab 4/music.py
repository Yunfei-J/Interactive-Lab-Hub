import sounddevice as sd
import numpy as np
import time

# Initialize parameters
A = 1  # Amplitude
frequency = 1000  # Fixed frequency
phi = 0  # Phase
sr = 44100  # Sample rate
num = 0
f_list = [194,779,284,156,732,739,145,995,573,672,183,95,529,194,779,284,156,732,739,145,995,573,672,183,95,529]


# Start the sound stream
sd_stream = sd.OutputStream(callback=None, channels=1, samplerate=sr, dtype='float32')
sd_stream.start()

# Define the time interval for changing the frequency (0.1 seconds)
change_interval = 0.1  # seconds
next_change_time = time.time() + change_interval

while num<len(f_list)-1:
    num += 1
    # Check if it's time to change the frequency
    if time.time() >= next_change_time:
        frequency = f_list[num]
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