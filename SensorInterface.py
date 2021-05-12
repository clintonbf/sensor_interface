import abc


class SensorInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return(hasattr(subclass, 'connect_to_port') and
               callable(subclass.connect_to_port) and
               hasattr(subclass, 'get_raw_data') and
               callable(subclass.get_raw_data) or
               NotImplemented)

    @abc.abstractmethod
    def connect_to_port(self, device: str, timeout:int, baud_rate: int):
        raise NotImplementedError

    @abc.abstractmethod
    def get_raw_data(self) -> bytes:
        raise NotImplementedError