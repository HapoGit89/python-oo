"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """setup serial Number generator starting from start"""
        self.start = start
        self.count = start
        self.serial = start

    def generate(self):
        """ generates unique serial number in decreasing fashion from start"""
        self.serial = self.count
        self.count += 1
        return self.serial
    
    def reset(self):
        """resets the serial number to start value"""
        self.count = self.start
        self.serial = self.start
    
