""" Here you can convert any units of temperature.
Remember: for converting from one unit to another all functions takes the parameter of the unit to to be converted.
Also only integers or floats supported as parameters.
"""


def celstofar(celsius):
    """ This function convert celsius to fahrenheit, with celsius as the parameter.."""
    fahrenheit = (9 * celsius) / 5 + 32
    return fahrenheit


def celstokelv(celsius):
    """ This function converts celsius to Kelvin, with celsius as parameter."""
    kelvin = celsius + 273.15
    return kelvin


def celctorank(celsius):
    """ This function converts celsius to Rankine, with celsius as parameter."""
    rankine = (celsius + 273.15) * 1.8
    return rankine


def celctoreau(celsius):
    """ This function converts celsius to Réaumur , with celsius as parameter."""
    reaumur = celsius * 0.8
    return reaumur


def fartocels(fahrenheit):
    """ This function converts fahrenheit to celsius, with fahrenheit as parameter."""
    celsius = 5 * (fahrenheit - 32) / 9
    return celsius


def fartokelv(fahrenheit):
    """ This function converts fahrenheit to kelvin, with fahrenheit as parameter."""
    kelvin = (fahrenheit + 459.67) / 1.8
    return kelvin


def fartorank(fahrenheit):
    """ This function converts fahrenheit to rankine, with fahrenheit as parameter."""
    rankine = (fahrenheit + 459.67)
    return rankine


def fartoreau(fahrenheit):
    """ This function converts fahrenheit to Réaumur, with fahrenheit as parameter."""
    reaumur = (fahrenheit - 32) * (4 / 9)
    return reaumur


def kelvtocels(kelvin):
    """ This function converts kelvin to celsius, with kelvin as parameter."""
    celsius = kelvin - 273.15
    return celsius


def kelvtofar(kelvin):
    """ This function converts kelvin to fahrenheit, with kelvin as parameter."""
    fahrenheit = (kelvin * 1.8) - 459.67
    return fahrenheit


def kelvtorank(kelvin):
    """ This function converts kelvin to Rankine, with kelvin as parameter."""
    rankine = (kelvin * 1.8)
    return rankine


def kelvtoreau(kelvin):
    """ This function converts kelvin to Reaumur, with kelvin as parameter."""
    Reaumur = (kelvin - 273.15) * 0.8
    return Reaumur


def ranktocels(rankine):
    """ This function converts Rankine to celsius, with Rankine as parameter."""
    celsius = (rankine - 491.67) / 1.8
    return celsius


def ranktofar(rankine):
    """ This function converts Rankine to fahrenheit, with Rankine as parameter."""
    fahrenheit = rankine - 459.67
    return fahrenheit


def ranktokelv(rankine):
    """ This function converts Rankine to kelvin, with Rankine as parameter."""
    kelvin = rankine / 1.8
    return kelvin


def ranktoreau(rankine):
    """ This function converts Rankine to Reaumur, with Rankine as parameter."""
    reaumur = (rankine - 491.67) * (4 / 9)
    return reaumur


def reautocels(reaumur):
    """ This function converts Reaumur to celsius, with Reaumur as parameter."""
    celsius = reaumur / 0.8
    return celsius


def reautofar(reaumur):
    """ This function converts Reaumur to celsius, with Reaumur as parameter."""
    fahrenheit = (reaumur * 2.25) + 32
    return fahrenheit


def reautokelv(reaumur):
    """ This function converts Reaumur to kelvin, with Reaumur as parameter."""
    kelvin = (reaumur * 1.25) + 273.15
    return kelvin


def reautorank(reaumur):
    """ This function converts Reaumur to rankine, with Reaumur as parameter."""
    rankine = (reaumur * 2.25) + 491.67
    return rankine

