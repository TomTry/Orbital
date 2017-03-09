class Craft(object):
    
    def __init__(self, mass):
        self._mass = mass
    
    @property    
    def mass(self):
        return (self._mass)
    
    @mass.setter
    def mass(self, value):
        self._mass = value
    
    def get_gravity_exerted(self):
        pass