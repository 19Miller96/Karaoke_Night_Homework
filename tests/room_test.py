import unittest

from src.room import Room

class TestRoom(unittest.TestCase):

    def test_room_number(self):
        self.room = Room(2)