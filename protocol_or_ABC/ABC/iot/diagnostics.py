from protocol_or_ABC.ABC.iot.device import Device


def collect_diagnostics(device: Device) -> None:
    print("Collecting to diagnostics server")
    status = device.status_update()
    print(f'Status: {status}')