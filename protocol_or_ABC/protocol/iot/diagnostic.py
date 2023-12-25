from typing import Protocol


class DiagnosticsSource(Protocol):
    def update_status(self, status: str) -> bool:
        ...


class RedisSource:
    def update_status(self, status: str) -> bool:
        match status:
            case "connected":
                return True
            case "disconnected":
                return False


class PostgresSource:

    def __init__(self):
        print('Реализовываем подключение к бд')
        self.connection = dict()

    def update_status(self, status: str) -> bool:
        self.connection[status] = True
        return self.connection[status]


def diagnostic_device(source: DiagnosticsSource, status) -> None:
    print("Connecting to diagnostic server...")
    status = source.update_status(status)
    print(f"The status was update to [{status}]")


diagnostic_device(PostgresSource(), "connected")
