from sensors import spec_dgs
from sensors import spec_dgs_reading


class co_sensor(spec_dgs):
    def __init__(self, uid: int, device: str, timeout: int, baud_rate: int):
        super().__init__(device, timeout, baud_rate)
        self.__uid = uid
        self.__reading = None

    def take_reading(self):
        raw_data = self.get_raw_data()

        self.__reading = spec_dgs_reading(self.__uid, raw_data)

    def get_co(self) -> float:
        f"""
        Gets carbon monoxide reading.

        :return: {float} 
        """

        return self.__reading.get_raw_sensor()

    def print_data(self):
        # for (k, v) in self.__reading.get_sensor_reading():
        #     print(k, v)

        d = self.__reading.get_sensor_reading()
        print("Type of d is ", type(d))
