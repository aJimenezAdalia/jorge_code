
from abc import ABC, abstractmethod
from utils import NUMBERS


class IpTranslation(ABC):
    """ Translate IP addresses."""
    def __init__(self, ip: str):
        """ Constructor class """
        self.ip = ip

    @abstractmethod
    def translation(self):
        print(self.ip)

    @abstractmethod
    def ip_class(self):
        pass


class BinaryTranslation(IpTranslation):
    def translation(self):
        """
        Translate decimal IP address into binary IP address
        """
        binary_ip = self.ip.split('.')
        binary_bytes = [byte[::-1] for byte in binary_ip]
        decimal_byte = []
        decimal_bytes = []
        for byte in binary_bytes:
            for index, bit in enumerate(list(byte)):
                bit = int(bit) * (2 ** int(index))
                decimal_byte.append(bit)
            decimal_bytes.append(sum(decimal_byte))
            decimal_byte.clear()
        ip_address = '.'.join(str(byte) for byte in decimal_bytes)
        return ip_address

    def ip_class(self):
        ip_address = self.ip
        return ip_address

    def ip_info(self):
        ip_type = 'binary'

        return 'IP TYPE:', ip_type, 'TRANSLATION:', self.translation()


class DecimalTranslation(IpTranslation):
    def translation(self):
        """
        Translate binary IP address into decimal IP address
        """
        decimal_ip = self.ip.split('.')
        binary_ip = []
        for byte in decimal_ip:
            result = int(byte)
            for value in NUMBERS:
                result -= value
                if result < 0:
                    binary_ip.append(0)
                    result += value
                else:
                    binary_ip.append(1)
            binary_ip.append('.')
        binary_ip = binary_ip
        ip_address = ''.join(str(bit) for bit in binary_ip)
        return ip_address[:-1]

    def ip_class(self):
        ip_address = self.translation()
        return ip_address

    def ip_info(self):
        ip_type = 'decimal'

        return 'IP TYPE:', ip_type, 'TRANSLATION:', self.translation()



