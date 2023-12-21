from protocol_or_ABC.protocol.iot.devices import Curtain, SmartSpeaker, HueLight

from protocol_or_ABC.protocol.iot.diagnostic import diagnostic_device
from protocol_or_ABC.protocol.iot.message import Message, MessageType
from protocol_or_ABC.protocol.iot.service import IOTService


def main() -> None:
    # Создаем сервис
    service = IOTService()

    # Создаем сущности устройств
    curtain = Curtain()
    speaker = SmartSpeaker()
    hue_light = HueLight()

    curtain_id = service.register_device(curtain)
    speaker_id = service.register_device(speaker)
    hue_light_id = service.register_device(hue_light)

    program_to_wake_up = [
        Message(curtain_id, MessageType.OPEN),
        Message(speaker_id, MessageType.PLAY_SONG, 'Kanye West - Good Morning'),
        Message(hue_light_id, MessageType.SWITCH_ON)
    ]

    program_to_sleep = [
        Message(curtain_id, MessageType.CLOSE, 'Занавески закрываются, для удобного сна'),
        Message(speaker_id, MessageType.PLAY_SONG),
        Message(hue_light_id, MessageType.COLOR, 'Включаю синий свет для комфортного сна')
    ]

    diagnostic_device(curtain)

    service.run_program(program_to_wake_up)
    service.run_program(program_to_sleep)


if __name__ == "__main__":
    main()
