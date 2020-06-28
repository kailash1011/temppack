""" Here you can convert any units of temperature."""
import class_basics
class converter:
    """ This is the class Converter."""
    def __init__(self):
        """ Lets Initialize the values.
        celsius & and fahrenheit are instance variables.
        There are no class variables."""
        self.celsius = 0
        self.fahrenheit = 0
    def celctofar(self,celc):
        """ This function convert celsius to fahrenheit."""
        self.fahrenheit = (9 * celc) / 5 + 32
        print(" For value in celsius: {} \n\tfahrenheit value is: {}".format(celc, self.fahrenheit))
    def fartocelc(self, far):
        """ This function converts fahrenheit to celcius"""
        self.celsius = 5 * (far - 32) / 9
        print("For value in fahrenheit: {} \n\tcelsius value is {}".format(far, self.celsius))


k = "Kailash"