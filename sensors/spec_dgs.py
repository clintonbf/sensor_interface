import SensorInterface
import serial


class spec_dgs(SensorInterface):
    """
        Credit for much of this code goes to Noah MacRitchie (noah21mac@gmail.com)
        and Andrey Goryelov (andrey.goryelov@gmail.com)
    """

    def __init__(self, device: str, timeout: int, baud_rate: int):
        self.__start_reading = 'c'
        self.__end_reading = 'R'
        self.__device = device
        self.__timeout = timeout
        self.__baud_rate = baud_rate

    def connect_to_port(self) -> serial:
        # TODO error checking?
        ser = serial.Serial(self.__device, self.__baud_rate, timeout=self.__timeout, parity=serial.PARITY_NONE)
        return ser

    def get_raw_data(self) -> bytes:
        ser = self.connect_to_port()
        ser.write(self.__start_reading.encode())
        line = ser.readline()
        ser.write(self.__end_reading.encode())

        return line