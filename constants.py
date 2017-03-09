# encoding: utf-8
from __future__ import absolute_import, division, print_function

from datetime import timedelta as _timedelta

from scipy.constants import kilo as _kilo

g = 6.67428e-11  

earth_mass                  = 5.97237e24
earth_radius_equatorial     = 6378.1
earth_mu                    = earth_mass  * g
earth_mean_radius           = 6371.0
earth_sidereal_day          = 138984
earth_eccentricity          = 0.0167086
earth_aphelion              = 152100000   * _kilo
earth_perihelion            = 147095000   * _kilo
earth_orbit_speed           = 108 * _kilo * 50
earth_distance_from_sun     = 149000 * _kilo

sun_mass                  = 1.98855e30
sun_radius_equatorial     = 695700
sun_mu                    = sun_mass  * g
sun_mean_radius           = sun_radius_equatorial

km_per_pixel              = 500000
