import RPi.GPIO
from time import sleep

class Board:
    
    def __init__(self):
        self.GPIO = RPi.GPIO
        self.GPIO.setmode(self.GPIO.BCM)
        self.GPIO.setwarnings(False)
        self.mode = self.GPIO.getmode()
        self.rpi_version = self.GPIO.VERSION

    def print_gpio_details(self):
        if self.mode == 11:
            mode = 'BCM'
        elif self.mode == 10:
            mode = 'BOARD'
        else:
            mode = 'Error'
        print('Board is set to mode ' + mode)
        print('RPi version is ' + str(self.rpi_version))

    def clean_up(self):
        self.GPIO.cleanup()

    def print_pin_assignments(self):
        for pin in range(1,41):
            current = self.GPIO.gpio_function(pin)
            if current == 1:
                func = 'GPIO.IN'
            elif current == 0:
                func == 'GPIO.OUT'
            elif current == 41:
                func == 'GPIO.SPI'
            elif current == 42:
                func == 'GPIO.I2C'
            elif current == 43:
                func == 'GPIOHARD_PWM'
            elif current == 40:
                func == 'GPIO.SERIAL'
            elif current == -1:
                func == 'GPIO.UNKNOWN'
            else:
                func == 'Error'            

            print('Pin ' + str(pin) + ' is currently set to ' + func)


if __name__ == "__main__":

    # main program
    rpi = Board()
    rpi.print_gpio_details()
    rpi.print_pin_assignments()





