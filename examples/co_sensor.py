from sensors import co_sensor

DEVICE = '/dev/ttyUSB0'
TIMEOUT = 10
BAUD_RATE = 9600

UUID = 5000


def main():
    co = co_sensor(UUID, DEVICE, TIMEOUT, BAUD_RATE)

    co.take_reading()
    co.print_data()


if __name__ == '__main__':
    main()