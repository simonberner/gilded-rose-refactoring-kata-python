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
        is_not_aged_brie = self.name != "Aged Brie"
        is_not_backstage_pass = self.name != "Backstage passes to a TAFKAL80ETC concert"
        is_not_sulfuras = self.name != "Sulfuras, Hand of Ragnaros"

        if is_not_aged_brie:
            if is_not_backstage_pass:
                if self.quality > 0:
                    if is_not_sulfuras:
                        self.quality = self.quality - 1
            else:
                if self.quality < 50:
                    self.quality = self.quality + 1
                    if not is_not_backstage_pass:
                        if self.sell_in < 11 and self.quality < 50:
                            self.quality = self.quality + 1
                        if self.sell_in < 6 and self.quality < 50:
                            self.quality = self.quality + 1
            # Updating sellIn when not Sulfuras
            if is_not_sulfuras:
                self.sell_in = self.sell_in - 1
            # Code smell: repeated conditional
            if self.sell_in < 0:
                # ifelse
                if is_not_backstage_pass:
                    if self.quality > 0:
                        if is_not_sulfuras:
                            self.quality = self.quality - 1
                else:
                    self.quality -= self.quality

        # it is aged_brie
        else:
            if self.quality < 50:
                self.quality = self.quality + 1
            self.sell_in = self.sell_in - 1
            if self.sell_in < 0 and self.quality < 50:
                self.quality = self.quality + 1

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
