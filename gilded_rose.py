# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_item()


class Item:
    AGED_BRIE = "Aged Brie"
    BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"
    SULFURAS = "Sulfuras, Hand of Ragnaros"

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def update_item(self):
        self.__decrease_day()

        self.__adjust_quality()

        self.__calc_quality_when_selling_date_reached()

    def __calc_quality_when_selling_date_reached(self):
        # Once the sell by date has passed, Quality degrades twice as fast (meaning an additional decrease of -1)
        if self.sell_in < 0:
            if self.name != Item.AGED_BRIE:
                if self.name != Item.BACKSTAGE_PASS:
                    if self.name != Item.SULFURAS and self.quality > 0:
                        # Decrease quality
                        self.quality = self.quality - 1
                # Quality drops to 0 after the concert for Backstage passes
                else:
                    self.quality = 0
            else:
                if self.quality < 50:
                    # Increase quality
                    self.quality = self.quality + 1

    def __adjust_quality(self):
        # Decrease the quality of normal item
        if self.name != Item.AGED_BRIE and self.name != Item.BACKSTAGE_PASS and self.name != Item.SULFURAS:
            if self.quality > 0:
                self.quality = self.quality - 1
        # Increase quality for special items
        else:
            if self.quality < 50:
                self.quality = self.quality + 1
                if self.name == Item.BACKSTAGE_PASS:
                    if self.sell_in < 11:
                        if self.quality < 50:
                            self.quality = self.quality + 1
                    if self.sell_in < 6:
                        if self.quality < 50:
                            self.quality = self.quality + 1

    def __decrease_day(self):
        if self.name != Item.SULFURAS:
            self.sell_in = self.sell_in - 1

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
