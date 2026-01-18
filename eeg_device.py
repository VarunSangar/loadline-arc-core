# hardware_interface/eeg_device.py

import numpy as np
import asyncio
from .device_config import USE_REAL_HARDWARE
from .ble_client import ARC_BLE_Client

class EEGDevice:
    def __init__(self):
        if USE_REAL_HARDWARE:
            self.ble = ARC_BLE_Client()
            asyncio.run(self.ble.connect())
        else:
            print("[EEG] Using simulated EEG")

    def read(self):
        if USE_REAL_HARDWARE:
            timestamp, eeg = asyncio.run(self.ble.read_packet())
            return np.array(eeg)
        else:
            return np.random.randn(8)
