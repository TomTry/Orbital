import unittest
import calculations
import craft
import bodies

class orbit_tests(unittest.TestCase):
    
    def setUp(self):
            self.earth = bodies.earth
    
    def test_orbit_speed(self):
        self.assertAlmostEqual(calculations.orbit_speed(self.kerbal, 119253, 80, 160), 2217, delta = 1)
        
class craft_tests(unittest.TestCase):
    
    def setUp(self):
        self.spaceship = craft.Craft(2)
    
    def test_craft_has_mass(self):
        self.assertIn("_mass", self.spaceship.__dict__)

    def test_gravity_on_craft(self):
        self.assertAlmostEqual(self.spaceship.get_gravity_exerted(), 14.41, delta = 0.5)