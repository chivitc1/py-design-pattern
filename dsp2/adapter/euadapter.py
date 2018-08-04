from socket_suppliers import EUSocket
from smartphone import SmartPhone


class EUAdapter:
    input_voltage = EUSocket.output_voltage
    output_voltage = SmartPhone.max_input_voltage