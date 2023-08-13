# -*- coding: utf-8 -*-

LEGENDARY_ITEMS = ['Sulfuras, Hand of Ragnaros']
LEGENDARY_ITEMS_STATUS = "Bitch I'm legendary!"
class GildedRose(object):

    def __init__(self, items):
        self.items = items
    # SELL'_IN RULES
    # sell_in value must be decremented each time that update quality method was called OK
    # Sulfura no need sell_in value -- sell_in == 0 OK

    # QUALITY RULES
    # Quando a data de venda do item tiver passado, a qualidade (`quality`) do item diminui duas vezes mais rapido. (if sell_in == 0, quality -= 2) OK
    # A qualidade (`quality`) do item não pode ser negativa OK

    # SPECIAL QUALITY UPDATE CONDITIONS
    # O "Queijo Brie envelhecido" (`Aged Brie`), aumenta sua qualidade (`quality`) em `1` unidade a medida que envelhece.
    # O item "Sulfuras" (`Sulfuras`), por ser um item lendário, não precisa ter uma data de venda (`SellIn`) e sua qualidade (`quality`) não precisa ser diminuida.
    # O item "Entrada para os Bastidores" (`Backstage Passes`), assim como o "Queijo Brie envelhecido", aumenta sua qualidade (`quality`) a medida que o dia da venda (`SellIn`) se aproxima;
    
    # Sulfuras its legendary, bitch... a update não muda seus valores de sell_in e quality que podem ser n/a - formatados em um método
    
    def sell_in_drop(self, item):
        item.sell_in -= 1
        return item
    
    def check_sell_in_date_to_update_quality(self, item):
        if item.sell_in == 0:
            item.quality -= 2
        else:
            item.quality -= 1

        return item
    
    def format_quality_value(self,item):
        if item.quality < 0:
            item.quality = 0
        
        return item

    def format_legendary_items(self,item):
        item.sell_in = LEGENDARY_ITEMS_STATUS
        item.quality = LEGENDARY_ITEMS_STATUS
        return item
    

    def update_quality(self):
        for item in self.items:
            if item.name not in LEGENDARY_ITEMS:
                self.sell_in_drop(item)
                self.check_sell_in_date_to_update_quality(item)
                self.format_quality_value(item)
            else:
                self.format_legendary_items(item)
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


