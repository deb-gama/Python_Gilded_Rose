# -*- coding: utf-8 -*-
class GildedRose(object):

    def __init__(self, items):
        self.items = items
    # SELL'_IN RULES
    # sell_in value must be decremented each time that update quality method was called OK
    # Sulfura no need sell_in value -- sell_in == 0 OK

    # QUALITY RULES
    # Quando a data de venda do item tiver passado, a qualidade (`quality`) do item diminui duas vezes mais rapido. (if sell_in == 0, quality -= 2) OK
    # A qualidade (`quality`) do item não pode ser negativa
    # O "Queijo Brie envelhecido" (`Aged Brie`), aumenta sua qualidade (`quality`) em `1` unidade a medida que envelhece.
    def sell_in_drop(self, item):
        if "Sulfuras" in item.name:
            item.sell_in = 0
        else: 
            item.sell_in -= 1
            
        return item
    
    def check_sell_in_date_to_update_quality(self, item):
        if item.sell_in == 0:
            item.quality -= 2
        else:
            item.quality -= 1

        return item
    
    def format_quality_value(self,item):
        ...

    def update_quality(self):
        for item in self.items:
            self.sell_in_drop(item)
            self.check_sell_in_date_to_update_quality(item)
            self.format_quality_value(item)
            # if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
            #     if item.quality > 0:
            #         if item.name != "Sulfuras, Hand of Ragnaros":
            #             item.quality = item.quality - 1
            # else:
            #     if item.quality < 50:
            #         item.quality = item.quality + 1
            #         if item.name == "Backstage passes to a TAFKAL80ETC concert":
            #             if item.sell_in < 11:
            #                 if item.quality < 50:
            #                     item.quality = item.quality + 1
            #             if item.sell_in < 6:
            #                 if item.quality < 50:
            #                     item.quality = item.quality + 1
            # if item.name != "Sulfuras, Hand of Ragnaros":
            #     item.sell_in = item.sell_in - 1
            # if item.sell_in < 0:
            #     if item.name != "Aged Brie":
            #         if item.name != "Backstage passes to a TAFKAL80ETC concert":
            #             if item.quality > 0:
            #                 if item.name != "Sulfuras, Hand of Ragnaros":
            #                     item.quality = item.quality - 1
            #         else:
            #             item.quality = item.quality - item.quality
            #     else:
            #         if item.quality < 50:
            #             item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


