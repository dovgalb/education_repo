from typing import Protocol


class DiagnosticsSource(Protocol):
    def update_status(self) -> str:
        ...


def diagnostic_device(source: DiagnosticsSource) -> None:
    print("Connecting to diagnostic server...")
    status = source.update_status()
    print(f"The status was update to [{status}]")