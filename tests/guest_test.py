import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):
    
    def test_guest_has_name(self):
        self.name = Guest("John Lennon")
