# encoding: utf-8

import constants as oc
from scipy.constants import kilo as _kilo

created_bodies = []

class Body(object):
    r"""Reference body for a Keplerian orbit.

    :param float mass: Mass (:math:`m`) [kg]
    :param float mu: Standard gravitational parameter (:math:`\mu`) [m\ :sup:`3`\ ·s\ :sup:`-2`]
    :param float mean_radius: Mean radius (:math:`r_\text{mean}`) [m]
    :param float equatorial_radius: Equatorial radius (:math:`r_\text{equat}`) [m]
    :param float polar_radius: Polar radius (:math:`r_\text{polar}`) [m]
    """
    def __init__(self, name, mass, mu, mean_radius, equatorial_radius, x_pos, y_pos):
        self.name = name
        self.mass = mass
        self.mu = mu
        self.mean_radius = mean_radius
        self.equatorial_radius = equatorial_radius
        self.position = [x_pos, y_pos]
        super(Body, self).__init__()
        created_bodies.append(self)

earth = Body(
     name = "earth",
     mass = oc.earth_mass,
     mu = oc.earth_mu,
     mean_radius = oc.earth_mean_radius,
     equatorial_radius = oc.earth_radius_equatorial,
     x_pos = 149000 * _kilo,
     y_pos = 0     
)

sun = Body(
    name = "sun",
    mass = oc.sun_mass,
    mu = oc.sun_mu,
    mean_radius = oc.sun_mean_radius,
    equatorial_radius = oc.sun_radius_equatorial,
    x_pos = 0,
    y_pos = 0
)



pass
#print(type(mun))