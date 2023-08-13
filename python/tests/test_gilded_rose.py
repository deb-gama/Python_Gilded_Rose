# -*- coding: utf-8 -*-
import unittest
import pytest

from gilded_rose import Item, GildedRose
from gilded_rose_test_base import GildedTestBase

class GildedRoseTest(GildedTestBase):
    
    def test_sell_in_must_be_decremented_when_update_quality_method_was_called(self):
        days = 2
        items_list = self.items
        gilded = GildedRose(items_list)

        for _ in range(days):
            gilded.update_quality()
        
        expected_result = [8,0,3,0,0,13,8,3,1]

        with self.subTest(expected_result = expected_result):
            result = []
            for item in items_list:
                result.append(item.sell_in)
            
            self.assertEqual(result, expected_result)


    def test_sell_in_must_be_zero_if_item_is_sulfuras(self):
        items_list = self.items
        gilded = GildedRose(items_list)
        expected_result = 0

        gilded.update_quality()

        with self.subTest(expected_result = expected_result):
            for item in items_list:
                if 'Sulfuras' in item.name:
                    self.assertEqual(item.sell_in,expected_result)



        

        
if __name__ == '__main__':
    unittest.main()
