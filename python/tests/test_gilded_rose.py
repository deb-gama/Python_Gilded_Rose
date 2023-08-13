# -*- coding: utf-8 -*-
import unittest
from python.gilded_rose import Item, GildedRose
from tests.gilded_rose_test_base import GildedTestBase

LEGENDARY_ITEMS = ['Sulfuras, Hand of Ragnaros']
class GildedRoseTest(GildedTestBase):
    
    def test_sell_in_must_be_decremented_when_update_quality_method_was_called(self):
        days = 2
        gilded = self.mocked_gilded

        for _ in range(days):
            gilded.update_quality()
        
        expected_result = [8,0,3,13,8,3,1]

        with self.subTest(expected_result = expected_result):
            result = []
            for item in self.items:
                if item.name not in LEGENDARY_ITEMS:
                    result.append(item.sell_in)
            
            self.assertEqual(result, expected_result)


    # def test_sell_in_always_must_be_zero_if_item_is_sulfuras(self):
    #     gilded = self.mocked_gilded
    #     expected_result = 0

    #     gilded.update_quality()

    #     with self.subTest(expected_result = expected_result):
    #         for item in self.items:
    #             if 'Sulfuras' in item.name:
    #                 self.assertEqual(item.sell_in,expected_result)


    def test_quality_must_be_decremented_once_when_update_quality_method_was_called(self):
        gilded = self.mocked_gilded
        gilded.update_quality()
        
        expected_result = [19,0,6,19,48,48,5]

        with self.subTest(expected_result = expected_result):
            result = []
            for item in self.items:
                if item.name not in LEGENDARY_ITEMS:
                    result.append(item.quality)
            
            self.assertEqual(result, expected_result)

    def test_quality_must_be_decremented_twice_if_sell_in_equals_zero(self):
        gilded = self.mocked_gilded
        gilded.update_quality()
        
        expected_result = [19,-0,6,19,48,48,5]

        with self.subTest(expected_result = expected_result):
            result = []
            for item in self.items:
                if item.name not in LEGENDARY_ITEMS:
                    result.append(item.quality)
            
            self.assertEqual(result, expected_result)

    def test_quality_must_never_be_negative(self):
        days = 3
        gilded = self.mocked_gilded

        for _ in range(days):
            gilded.update_quality()
        
        expected_result = [17,0,4,17,46,46,2]

        with self.subTest(expected_result = expected_result):
            result = []
            for item in self.items:
                if item.name not in LEGENDARY_ITEMS:
                    result.append(item.quality)
            
            self.assertEqual(result, expected_result)

    def test_brie_must_have_the_quality_incremented(self):
        days = 2
        gilded = self.mocked_gilded

        for _ in range(days):
            gilded.update_quality()
        
        expected_result = [18,2,5,17,46,46,2]

        with self.subTest(expected_result = expected_result):
            result = []
  
            for item in self.items:
                result.append(item.quality)
            
            self.assertEqual(result, expected_result)

            print(result)



        

        
if __name__ == '__main__':
    unittest.main()

    
