# hardware_interface/packet_parser.py

import struct

def parse_eeg_packet(packet: bytes, num_channels: int):
    """
    Packet format:
    [0–3]   uint32 timestamp (ms)
    [4–...] int32 EEG samples
    """

    timestamp = struct.unpack_from("<I", packet, 0)[0]
    eeg = []

    offset = 4
    for _ in range(num_channels):
        val = struct.unpack_from("<i", packet, offset)[0]
        eeg.append(val)
        offset += 4

    return timestamp, eeg
