# encoding: utf-8

import constants as oc

__all__ = [
    'mercury',
    'mun',
    'venus',
    'earth',
    'mars',
    'jupiter',
    'saturn',
    'uranus',
    'neptune',
]


class Body(object):
    r"""Reference body for a Keplerian orbit.

    :param float mass: Mass (:math:`m`) [kg]
    :param float mu: Standard gravitational parameter (:math:`\mu`) [m\ :sup:`3`\ ·s\ :sup:`-2`]
    :param float mean_radius: Mean radius (:math:`r_\text{mean}`) [m]
    :param float equatorial_radius: Equatorial radius (:math:`r_\text{equat}`) [m]
    :param float polar_radius: Polar radius (:math:`r_\text{polar}`) [m]
    :param apoapsis_names: Specific apoapsis name(s) for body. E.g. `apogee` for earth.
    :type apoapsis_names: String, or list of strings.
    :param periapsis_names: Specific periapsis name(s) for body.
    :type apoapsis_names: String, or list of strings.
    :param plot_color: Color understood by Matplotlib, e.g. '#FF0000' or 'r'
    """
    def __init__(self, mass, mu, mean_radius, equatorial_radius, polar_radius):
        self.mass = mass
        self.mu = mu
        self.mean_radius = mean_radius
        self.equatorial_radius = equatorial_radius
        self.polar_radius = polar_radius
        super(Body, self).__init__()

mun = Body(
    mass = oc.mun_mass,
    mu = oc.mun_mu,
    mean_radius = oc.mun_radius_mean,
    equatorial_radius = oc.mun_radius_equatorial,
    polar_radius = oc.mun_radius_polar
)



print(mun)