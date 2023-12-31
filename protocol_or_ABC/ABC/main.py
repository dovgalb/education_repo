from protocol_or_ABC.ABC.iot.devices import HueLight, SmartSpeaker, Curtains
from protocol_or_ABC.ABC.iot.diagnostics import collect_diagnostics
from protocol_or_ABC.ABC.iot.message import Message, MessageType
from protocol_or_ABC.ABC.iot.service import IOTService


def main() -> None:
    # create a IOT service
    service = IOTService()

    # create and register a few devices
    hue_light = HueLight()
    speaker = SmartSpeaker()
    curtains = Curtains()
    hue_light_id = service.register_device(hue_light)
    speaker_id = service.register_device(speaker)
    curtains_id = service.register_device(curtains)

    # create a few programs
    wake_up_program = [
        Message(hue_light_id, MessageType.SWITCH_ON),
        Message(speaker_id, MessageType.SWITCH_ON),
        Message(speaker_id, MessageType.PLAY_SONG, "Miles Davis - Kind of Blue"),
        Message(curtains_id, MessageType.OPEN),
    ]

    sleep_program = [
        Message(hue_light_id, MessageType.SWITCH_OFF),
        Message(speaker_id, MessageType.SWITCH_OFF),
        Message(curtains_id, MessageType.CLOSE),
    ]

    # run the programs
    service.run_program(wake_up_program)
    service.run_program(sleep_program)

    # collect some diagnostics
    collect_diagnostics(hue_light)


if __name__ == "__main__":
    main()