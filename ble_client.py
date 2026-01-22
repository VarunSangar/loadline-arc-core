from .ble_adapter import BLEAdapter

class BLEClient(BLEAdapter):
    def __init__(self, address):
        self.address = address
        self.connect(address)

    def read(self):
        return b"\x00\x01\x00\x02"
