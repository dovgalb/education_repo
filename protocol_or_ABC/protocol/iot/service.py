import string
import random
from typing import Protocol

from protocol_or_ABC.protocol.iot.message import Message, MessageType


def generate_id(length: int = 8):
    return ''.join(random.choice(string.ascii_uppercase))


class Device(Protocol):
    def connect(self) -> None:
        ...

    def disconnect(self) -> None:
        ...

    def send_message(self, msg: MessageType) -> None:
        ...

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
            self.devices[msg.device_id].send_message(msg.message_type, msg.data)
        print("=====END PROGRAM=====")
