from protocol_or_ABC.protocol.iot.message import MessageType


class HueLight:
    def connect(self) -> None:
        print("Connecting to HueLight")

    def disconnect(self) -> None:
        print("Disconnecting from HueLight")

    def send_message(self, msg: MessageType, data: str) -> None:
        print(f"sending from HueLight message type: \"{msg.name}\" with data: \"{data}\"")

    def update_status(self) -> str:
        return 'hue_light_status_is_ok'


class SmartSpeaker:
    def connect(self) -> None:
        print("Connecting to SmartSpeaker")

    def disconnect(self) -> None:
        print('connecting to SmartSpeaker')

    def send_message(self, msg: MessageType, data: str) -> None:
        print(f"sending from SmartSpeaker message type: \"{msg.name}\" with data: \"{data}\"")

    def update_status(self) -> str:
        return "smart_speaker_status_is_ok"


class Curtain:
    def connect(self) -> None:
        print("Connecting to Curtain")

    def disconnect(self) -> None:
        print('disconnecting from Curtain')

    def send_message(self, msg: MessageType, data: str) -> None:
        print(f"sending from Curtain message type: \"{msg.name}\" with data: \"{data}\"")

    def update_status(self) -> str:
        return "curtain_status_is_ok"