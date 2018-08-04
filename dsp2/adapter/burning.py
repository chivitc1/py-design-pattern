import smartphone
from socket_suppliers import EUSocket


phone = smartphone.SmartPhone()
phone.charge(EUSocket.output_voltage)