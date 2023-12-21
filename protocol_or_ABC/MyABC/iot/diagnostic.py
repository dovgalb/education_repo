from protocol_or_ABC.MyABC.iot.device import Device


def diagnostic_device(device: Device) -> None:
    print("Connecting to diagnostic server...")
    status = device.update_status()
    print(f"The status was update to [{status}]")