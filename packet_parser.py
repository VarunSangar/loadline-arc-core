import struct
import numpy as np

def parse_eeg_packet(packet: bytes) -> np.ndarray:
    values = struct.unpack(f"{len(packet)//2}h", packet)
    return np.array(values)
