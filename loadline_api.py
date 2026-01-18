import requests
import time

class LoadlineAPI:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def send_cli(self, cli, subject):
        payload = {
            "timestamp": time.time(),
            "cli": cli,
            "subject": subject
        }

        try:
            requests.post(self.endpoint, json=payload, timeout=1)
        except:
            pass
