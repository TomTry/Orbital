# encoding: utf-8
from __future__ import absolute_import, division, print_function

from datetime import timedelta as _timedelta

from scipy.constants import kilo as _kilo

# IAU 2009 System of Astronomical Constants
# Updated as of 2014

constant_of_gravitation = 6.67428e-11  # m^3 kg^-1 s^-2

mun_mass = 9.7600236e20
mun_radius_equatorial     = 200       * _kilo
mun_mu     = mun_mass     * constant_of_gravitation
mun_radius_polar= mun_radius_mean = mun_radius_equatorial

mun_sidereal_day = 138984