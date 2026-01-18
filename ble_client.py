# hardware_interface/ble_client.py

import asyncio
from bleak import BleakClient, BleakScanner
from .device_config import *
from .packet_parser import parse_eeg_packet

class ARC_BLE_Client:
    def __init__(self):
        self.client = None

    async def connect(self):
        devices = await BleakScanner.discover()
        target = next(d for d in devices if BLE_DEVICE_NAME in d.name)

        self.client = BleakClient(target.address)
        await self.client.connect()
        print("[BLE] Connected to ARC headband")

    async def read_packet(self):
        packet = await self.client.read_gatt_char(BLE_CHARACTERISTIC_UUID)
        return parse_eeg_packet(packet, NUM_CHANNELS)
