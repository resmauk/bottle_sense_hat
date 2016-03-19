
class RGB_Led:
    def __init__(self, gpio_object, r, g, b):
        self.__red_pin = r
        self.__green_pin = g
        self.__blue_pin = b
        self.__outputs = [self.__red_pin, self.__green_pin, self.__blue_pin]
        self.__board = gpio_object

        self.__setup_pins()

    def __setup_pins(self):
        print('DEBUG: Setting up outputs')

        for pin in self.__outputs:
            self.__board.GPIO.setup(pin, self.__board.GPIO.OUT)
        
    def red_on(self):
        ''' Turn's on red led '''
        self.turn_all_off()
        self.__board.GPIO.output(self.__red_pin, self.__board.GPIO.HIGH)

    def green_on(self):
        ''' Turn's on green led '''
        self.turn_all_off()
        self.__board.GPIO.output(self.__green_pin, self.__board.GPIO.HIGH)

    def blue_on(self):
        self.turn_all_off()
        ''' Turn's on blue led '''
        self.__board.GPIO.output(self.__blue_pin, self.__board.GPIO.HIGH)

    def turn_all_off(self):
        ''' Turn's all LEDs off '''
        for pin in self.__outputs:
            self.__board.GPIO.output(pin, self.__board.GPIO.LOW)

if __name__ == "__main__":
    from board import Board    
    from time import sleep
    B = Board()
    led = RGB_Led(B, 21, 20, 16)

    led.red_on()
    sleep(1)
    led.turn_all_off()
    led.green_on()
    sleep(1)
    led.turn_all_off()
    led.blue_on()
    sleep(1)
    led.turn_all_off()

    
