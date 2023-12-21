from abc import ABC, abstractmethod
from protocol_or_ABC.MyABC.iot.message import MessageType


class Device(ABC):
    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def disconnect(self) -> None:
        pass

    @abstractmethod
    def send_message(self, msg: MessageType, data: str) -> None:
        pass

    @abstractmethod
    def update_status(self) -> str:
        pass
