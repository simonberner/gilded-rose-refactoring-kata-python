# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_item()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def update_item(self):
        # If not Aged Brie and not Backstage passes
        is_aged_brie = self.name != "Aged Brie"

        if is_aged_brie and self.name != "Backstage passes to a TAFKAL80ETC concert":
            if self.quality > 0:
                if self.name != "Sulfuras, Hand of Ragnaros":
                    self.quality = self.quality - 1
        else:
            if self.quality < 50:
                self.quality = self.quality + 1
                if self.name == "Backstage passes to a TAFKAL80ETC concert":
                    if self.sell_in < 11:
                        if self.quality < 50:
                            self.quality = self.quality + 1
                    if self.sell_in < 6:
                        if self.quality < 50:
                            self.quality = self.quality + 1
        # Updating sellIn when not Sulfuras
        if self.name != "Sulfuras, Hand of Ragnaros":
            self.sell_in = self.sell_in - 1
        # Code smell: repeated conditional
        if self.sell_in < 0:
            if is_aged_brie:
                if self.name != "Backstage passes to a TAFKAL80ETC concert":
                    if self.quality > 0:
                        if self.name != "Sulfuras, Hand of Ragnaros":
                            self.quality = self.quality - 1
                else:
                    self.quality -= self.quality
            else:
                if self.quality < 50:
                    self.quality = self.quality + 1

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
