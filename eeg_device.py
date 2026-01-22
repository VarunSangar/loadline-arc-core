# hardware_interface/eeg_device.py

import numpy as np
from core.packet_parser import parse_eeg_packet

class EEGDevice:
    def __init__(self, client=None):
        self.client = client

    def read(self):
        raw = self.client.read() if self.client else b"\x01\x02"
        return parse_eeg_packet(raw)
