import numpy as np
import time

class EEGSimulator:
    def __init__(self, channels=32, fs=256):
        self.channels = channels
        self.fs = fs
        self.t = 0.0

    def read(self):
        dt = 1 / self.fs
        self.t += dt

        alpha = np.sin(2 * np.pi * 10 * self.t)
        beta  = np.sin(2 * np.pi * 20 * self.t) * 0.6
        theta = np.sin(2 * np.pi * 6  * self.t) * 0.4

        noise = np.random.randn(self.channels) * 0.1

        eeg = alpha + beta + theta + noise
        return eeg
