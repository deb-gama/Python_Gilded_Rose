# -*- coding: utf-8 -*-
import unittest
from python.gilded_rose import Item, GildedRose
from tests.gilded_rose_test_base import GildedTestBase

LEGENDARY_ITEMS = ['Sulfuras, Hand of Ragnaros']
SPECIAL_ITEMS = ['Aged Brie', 'Backstage passes to a TAFKAL80ETC concert']
LEGENDARY_ITEMS_STATUS = "Bitch I'm legendary!"

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


    def test_sell_in_always_must_be_a_personal_legendary_status_info_if_item_is_sulfuras(self):
        gilded = self.mocked_gilded
        expected_result = LEGENDARY_ITEMS_STATUS

        gilded.update_quality()

        with self.subTest(expected_result = expected_result):
            for item in self.items:
                if 'Sulfuras' in item.name:
                    self.assertEqual(item.sell_in,expected_result)


    # def test_quality_must_be_decremented_once_when_update_quality_method_was_called(self):
    #     gilded = self.mocked_gilded
    #     gilded.update_quality()
        
    #     expected_result = [19,6,5]

    #     with self.subTest(expected_result = expected_result):
    #         result = []
    #         for item in self.items:
    #             if item.name not in LEGENDARY_ITEMS and item.name not in SPECIAL_ITEMS:
    #                 result.append(item.quality)
            
    #         self.assertEqual(result, expected_result)

    # def test_quality_must_be_decremented_twice_if_sell_in_equals_zero(self):
    #     # TODO criar item com condição que deixe o sell in igual zero e que não seja brie nem backstage para que o teste específico pegue
    #     gilded = self.mocked_gilded
    #     gilded.update_quality()
        
    #     expected_result = [19,6,5]

    #     with self.subTest(expected_result = expected_result):
    #         result = []
    #         for item in self.items:
    #             if item.name not in LEGENDARY_ITEMS and item.name not in SPECIAL_ITEMS:
    #                 result.append(item.quality)
            
    #         self.assertEqual(result, expected_result)

    def test_quality_must_never_be_negative(self):
        days = 3
        gilded = self.mocked_gilded

        for _ in range(days):
            gilded.update_quality()
        
        expected_result = [26,3,16,23,52,52,15]

        with self.subTest(expected_result = expected_result):
            result = []
            for item in self.items:
                if item.name not in LEGENDARY_ITEMS:
                    result.append(item.quality)
            
            self.assertEqual(result, expected_result)

    def test_special_items_must_have_the_quality_incremented(self):
        days = 2
        gilded = self.mocked_gilded

        for _ in range(days):
            gilded.update_quality()
        
        expected_result = [24,2,13,22,51,51,12]

        with self.subTest(expected_result = expected_result):
            result = []
  
            for item in self.items:
                if item.name not in LEGENDARY_ITEMS:
                    result.append(item.quality)
            
            self.assertEqual(result, expected_result)

    
    def test_quality_must_be_incremented_twice_if_the_sell_in_date_is_equal_or_less_10(self):
        days = 2
        gilded = self.mocked_gilded

        for _ in range(days):
            gilded.update_quality()
        
        expected_result = [24,13,12]

        with self.subTest(expected_result = expected_result):
            result = []
  
            for item in self.items:
                if item.name not in LEGENDARY_ITEMS and item.name not in SPECIAL_ITEMS:
                    result.append(item.quality)
            
            self.assertEqual(result, expected_result)

    def test_conjured_items_must_have_quality_decremented_twice(self):
        gilded = self.mocked_gilded
        gilded.update_quality()
        
        expected_result = [22,10,4]

        with self.subTest(expected_result = expected_result):
            result = []
  
            for item in self.items:
                if item.name not in LEGENDARY_ITEMS and item.name not in SPECIAL_ITEMS:
                    result.append(item.quality)
            
            self.assertEqual(result, expected_result)

 
        

    # def test_quality_must_be_incremented_three_times_if_the_sell_in_date_is_equal_or_less_5(self):
    #     ...

    # def test_quality_must_be_zero_if_the_sell_in_is_equal_zero(self):
    #     ...



        

        
if __name__ == '__main__':
    unittest.main()

    
