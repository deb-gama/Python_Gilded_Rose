import unittest
from gilded_rose import Item, GildedRose

def gilded_mocker(items):
    gilded_mock = GildedRose(items)

    return gilded_mock

class GildedTestBase(unittest.TestCase):
    def setUp(self) -> None:
        self.items = [
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
            Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
        ]

        self.mocked_gilded = gilded_mocker(items=self.items)
        
        return super().setUp()
    
    def update_itens_simulator(self,days:int, itens:list):
        data_by_day = {}

        days_range = days + 1
        for day in range(days_range):
            data_by_day.setdefault(f'day {day}',[])
            for item in itens:  
                data_by_item = {
                    'name': item.name,
                    'sell_in': item.sell_in,
                    'quality': item.quality
                }

                data_by_day.get(f'day {day}').append(data_by_item)
        GildedRose(self.items).update_quality()
        return data_by_day


