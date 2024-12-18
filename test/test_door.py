import unittest
from door import Door

class TestDoor(unittest.TestCase):
    def test_initial_state(self):
        door = Door()
        self.assertFalse(door.locked)

    def test_lock(self):
        door = Door()
        door.lock()
        self.assertTrue(door.locked)
        
if __name__ == '__main__':
    unittest.main()