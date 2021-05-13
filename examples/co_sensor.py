from sensors import co_sensor, spec_dgs

DEVICE = '/dev/ttyUSB0'
TIMEOUT = 10
BAUD_RATE = 9600

UUID = 5000


def main():
    co = co_sensor(UUID, DEVICE, TIMEOUT, BAUD_RATE)

    co.take_reading()
    co.print_data()

    # spec_dgs_instance = spec_dgs(DEVICE, TIMEOUT, BAUD_RATE)


if __name__ == '__main__':
    main()