from math import sqrt as root
import bodies
import constants
from scipy.constants import kilo as _kilo

def orbit_speed(body, distance_from_surface, periapsis, apoapsis):
    
    if type(body) != bodies.Body:
        raise TypeError("'body' argument was not a bodies.Body object")
   
    semi_major_axis = ((periapsis * _kilo) + (body.equatorial_radius * 2) + (apoapsis * _kilo))/2
    orbit_speed = root(body.mu * ((2 / (distance_from_surface + body.equatorial_radius)) - (1/semi_major_axis)))
    pass
    return(orbit_speed)

def force_between_two_planets(body1, body2):
    if type(body1) != bodies.Body:
        raise TypeError("'body1' argument was not a bodies.Body object")
    
    if type(body2) != bodies.Body:
        raise TypeError("'body2' argument was not a bodies.Body object")
    
    force = constants.constant_of_gravitation