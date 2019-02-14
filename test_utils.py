# test_utils.py
# Author: Sébastien Combéfis
# Version: February 8, 2018

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(utils.fact(3), 6)
        self.asserEqual(utils.fact(4), 24)
        pass
    
    def test_roots(self):
        self.asserEqual(utils.roots(1,-2,3),(1,0))
        pass
    
    def test_integrate(self):
        self.almotsEqual(utils.integrate("x", 3,9),72)
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
