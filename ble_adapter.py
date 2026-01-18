import numpy as np

class BLEEEGAdapter:
    def __init__(self, device_name="ARC_HEADBAND"):
        self.device_name = device_name
        self.connected = False

    def connect(self):
        print(f"[BLE] Connecting to {self.device_name}...")
        self.connected = True

    def read(self):
        if not self.connected:
            raise RuntimeError("BLE device not connected")

        # Replace with real BLE packet parsing
        return np.zeros(32)
