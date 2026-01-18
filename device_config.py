# hardware_interface/device_config.py

USE_REAL_HARDWARE = False  # Flip this when headband is ready

BLE_DEVICE_NAME = "ARC-EEG"
BLE_SERVICE_UUID = "12345678-1234-5678-1234-56789abcdef0"
BLE_CHARACTERISTIC_UUID = "abcdef01-1234-5678-1234-56789abcdef0"

SAMPLE_RATE_HZ = 250
NUM_CHANNELS = 8  # Start with 8, scalable to 16
BYTES_PER_SAMPLE = 4  # int32 per channel
