

from day13 import *

import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self._starts = dict()

    
    def test_jump_to_next_step1(self):
        self.assertEqual(jump_to_next_multiplier(7, 1, (13, 1), self._starts), 11)

    def test_jump_to_next_step2(self):
        self.assertEqual(jump_to_next_multiplier(7, 11, (59, 4), self._starts), 50)


    def test_jump_to_next_step3(self):
        self.assertEqual(jump_to_next_multiplier(7, 50, (31, 6), self._starts), 70)


    def test_jump_to_next_step4(self):
        self.assertEqual(jump_to_next_multiplier(7, 70, (13, 1), self._starts), 76)


    def test_jump_to_next_step5(self):
        self.assertEqual(jump_to_next_multiplier(7, 76, (59, 4), self._starts), 109)

    
    def test_jump_to_next_from_second(self):
        self.assertEqual(jump_to_next_multiplier(7, 152681, (13, 1), self._starts), 152683)


    def test_jump_to_next_from_third(self):
        self.assertEqual(jump_to_next_multiplier(7, 152675, (59, 4), self._starts), 152683)


    def test_jump_to_next_from_fourth(self):
        self.assertEqual(jump_to_next_multiplier(7, 152679, (31, 6), self._starts), 152683)


    def test_jump_to_next_from_end(self):
        self.assertEqual(jump_to_next_multiplier(7, 152681, (19, 7), self._starts), 152683)

        

if __name__ == '__main__':
    unittest.main()
