from protocol_or_ABC.ABC.iot.device import Device
from protocol_or_ABC.ABC.iot.message import MessageType


class HueLight(Device):
    # def connect(self):
    #     print('Connecting to Hue Light...')

    def disconnect(self):
        print('Disconnecting from Hue Light...')

    def send_message(self, message_type: MessageType, data: str) -> None:
        print(
            f"Hue light handling message of type {message_type.name} with data [{data}]."
        )

    def status_update(self) -> str:
        return 'hue_light_status_ok'


class SmartSpeaker(Device):
    def connect(self):
        print('Connecting to Smart Speaker...')

    def disconnect(self):
        print('Disconnecting from smart speaker...')

    def send_message(self, message_type: MessageType, data: str) -> None:
        print(f'Smart Speaker handling message of type {message_type.name} with data [{data}].')

    def status_update(self):
        return 'smart_speaker_status_ok'


class Curtains(Device):
    def connect(self):
        print('Connecting to Curtains...')

    def disconnect(self):
        print('Disconnecting from Curtains...')

    def send_message(self, message_type: MessageType, data: str) -> None:
        print(f'Curtains handling message of type {message_type.name} with data [{data}].')

    def status_update(self):
        return 'curtains_status_ok'