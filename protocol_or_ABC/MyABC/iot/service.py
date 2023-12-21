import string
import random

from protocol_or_ABC.MyABC.iot.device import Device
from protocol_or_ABC.MyABC.iot.message import Message


def generate_id(length: int = 8):
    return ''.join(random.choice(string.ascii_uppercase))


class IOTService:
    def __init__(self):
        self.devices: dict[str, Device] = {}

    def register_device(self, device: Device) -> str:
        device.connect()
        device_id = generate_id()
        self.devices[device_id] = device
        return device_id

    def unregister_device(self, device_id: str) -> None:
        self.devices[device_id].disconnect()
        del self.devices[device_id]

    def get_device(self, device_id: str) -> Device:
        return self.devices[device_id]

    def run_program(self, messages: list[Message]) -> None:
        print("=====RUN PROGRAM=====")
        for msg in messages:
            print(self.devices[msg.device_id].send_message(msg.message_type, msg.data))
        print("=====END PROGRAM=====")
