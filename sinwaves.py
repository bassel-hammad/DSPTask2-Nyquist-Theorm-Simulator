import numpy as np


MAX_SAMPLES = 10000


class SineWave():
    def __init__(self, amplitude=1.0, frequency=1.0):
        self._amplitude = amplitude
        self._frequency = frequency  # Use a private attribute for frequency
        self.Xaxis = np.linspace(0, 2 * np.pi, 10000)
        self.Yaxis = self._amplitude * np.sin(2 * np.pi * self._frequency * self.Xaxis)
        self.update_data()

    def add(self, sinwaves1):
        return sinwaves1.Yaxis + self.Yaxis

    def get_frequency(self):
        return self._frequency  # Return the private frequency attribute

    def set_frequency(self, new_frequency):
        self._frequency = new_frequency
        self.update_data()

    def get_amplitude(self):
        return self._amplitude  # Return the private frequency attribute

    def set_amplitude(self, new_amplitude):
        self._amplitude = new_amplitude
        self.update_data()

    def update_data(self, num_points=10000,num_periods=1):
        # Generate the X-axis values (time)
        self.Xaxis = np.linspace(0, 2 *num_periods* np.pi, num_points)

        # Generate the Y-axis values based on the current frequency and amplitude
        self.Yaxis = self._amplitude * np.sin(2 * np.pi * self._frequency * self.Xaxis)
