from dataclasses import dataclass
from enum import Enum, auto


class MessageType(Enum):
    SWITCH_ON = auto()
    SWITCH_OFF = auto()
    COLOR = auto()
    PLAY_SONG = auto()
    PAUSE_SONG = auto()
    OPEN = auto()
    CLOSE = auto()


@dataclass
class Message():
    device_id: str
    message_type: MessageType
    data: str = ''
