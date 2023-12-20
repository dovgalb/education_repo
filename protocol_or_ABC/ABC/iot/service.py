import string
import random

from protocol_or_ABC.ABC.iot.device import Device
from protocol_or_ABC.ABC.iot.message import Message


def generate_id(length: int = 8):
    return ''.join(random.choice(string.ascii_uppercase, k=length))


class IOTService:
    def __init__(self):
        self.devices: dict[str, Device] = {}

    def register_device(self, device: Device) -> str:
        device.connect()
        device_id = generate_id
        self.devices[device_id] = device
        return device_id

    def unregister_device(self, device_id: str) -> None:
        self.devices[device_id].disconnect()
        del self.devices[device_id]

    def get_device(self, device_id: str) -> Device:
        return self.devices[device_id]

    def run_program(self, program: list[Message]) -> None:
        print('====RUNNING PROGRAM====')
        for message in program:
            self.devices[message.device_id].send_message(message.msg_type, message.data)
        print('====END OF PROGRAM====')


