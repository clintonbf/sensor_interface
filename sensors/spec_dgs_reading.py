from datetime import date

DATA_INDICES = {
    "serial_number": 0,
    "ppb": 1,
    "temperature": 2,
    "relative_humidity": 3,
    "raw_sensor": 4,
    "temp_digital": 5,
    "rh_digital": 6,
    "day": 7,
    "hour": 8,
    "minute": 9,
    "second": 10
}


class spec_dgs_reading:
    def __init__(self, uid: int, reading: bytes):
        self.__uid = uid
        self.__raw_reading = reading
        self.__reading = self.parse_reading()
        self.__timestamp = date.today()

    def parse_reading(self):
        raw_data = self.__raw_reading.decode().split()
        reading = []

        for i in range(0, len(raw_data)):
            pre_reading = raw_data[i].split(",")
            reading.append(pre_reading[0])

        return reading

    def get_uid(self):
        return self.__uid

    def get_serial_number(self) -> str:
        return str(self.__reading[DATA_INDICES["serial_number"]])

    def get_ppb(self) -> float:
        return float(self.__reading[DATA_INDICES["ppb"]])

    def get_temperature(self) -> float:
        f"""
        Gets the temperature reading of the sensor. Units in Kelvin
        
        :return: {float} 
        """
        conversion_factor = 273.15

        temp_in_celsius = float(self.__reading[DATA_INDICES["temperature"]])

        return temp_in_celsius + conversion_factor

    def get_relative_humidity(self) -> float:
        return float(self.__reading[DATA_INDICES["relative_humidity"]])

    def get_raw_sensor(self):
        return self.__reading[DATA_INDICES["raw_sensor"]]

    def get_temperature_digital(self) -> float:
        return float(self.__reading[DATA_INDICES["temp_digital"]])

    def get_relative_humidity_digital(self) -> float:
        return float(self.__reading[DATA_INDICES["rh_digital"]])

    def get_day(self):
        return self.__reading[DATA_INDICES["day"]]

    def get_hour(self) -> int:
        return int(self.__reading[DATA_INDICES["hour"]])

    def get_minute(self) -> int:
        return int(self.__reading[DATA_INDICES["minute"]])

    def get_second(self) -> int:
        return int(self.__reading[DATA_INDICES["second"]])

    def get_timestamp(self):
        return self.__timestamp

    def get_sensor_reading(self):
        reading = {
            "uid": self.get_uid(),
            "serial_number": self.get_serial_number(),
            "ppb": self.get_ppb(),
            "temperature": self.get_temperature(),
            "relative_humidity": self.get_relative_humidity(),
            "raw_sensor": self.get_raw_sensor(),
            "temperature_digital": self.get_temperature_digital(),
            "relative_humidity_digital": self.get_relative_humidity_digital(),
            "day": self.get_day(),
            "hour": self.get_hour(),
            "minute": self.get_minute(),
            "second": self.get_second()
        }

        return reading
