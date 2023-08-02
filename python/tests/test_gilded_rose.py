# -*- coding: utf-8 -*-
import unittest
import pytest

from python.gilded_rose import Item, GildedRose
from gilded_rose_test_base import GildedTestBase

class GildedRoseTest(GildedTestBase):
    
    def test_sell_in_must_be_decremented_as_the_days_goes_by(self):
        days = 2
        items_list = self.items
        gilded = GildedRose(items_list)

        for _ in range(days):
            gilded.update_quality()
        
        expected_result = [8,0,3,-2,-3,13,8,3,1]

        with self.subTest(expected_result = expected_result):
            result = []
            for item in items_list:
                result.append(item.sell_in)
            
            self.assertEqual(result, expected_result)




        

        
if __name__ == '__main__':
    unittest.main()
