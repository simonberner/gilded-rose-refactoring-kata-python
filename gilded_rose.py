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
        is_aged_brie = self.name == "Aged Brie"
        is_backstage_pass = self.name == "Backstage passes to a TAFKAL80ETC concert"
        is_sulfuras = self.name == "Sulfuras, Hand of Ragnaros"

        if not is_aged_brie:
            if not is_backstage_pass:
                if not is_sulfuras:
                    self.calculate_normal_item()
            else:
                self.calculate_backstage_pass()
        else:
            self.calculate_aged_brie()

    def calculate_normal_item(self):
        if self.quality > 0:
            self.quality = self.quality - 1
        self.sell_in = self.sell_in - 1
        if self.sell_in < 0 < self.quality:
            self.quality = self.quality - 1

    def calculate_backstage_pass(self):
        if self.quality < 50:
            self.quality = self.quality + 1
            if self.sell_in < 11 and self.quality < 50:
                self.quality = self.quality + 1
            if self.sell_in < 6 and self.quality < 50:
                self.quality = self.quality + 1
        self.sell_in = self.sell_in - 1
        if self.sell_in < 0:
            self.quality -= self.quality

    def calculate_aged_brie(self):
        self.sell_in = self.sell_in - 1
        if self.quality < 50:
            self.quality = self.quality + 1
        if self.sell_in < 0 and self.quality < 50:
            self.quality = self.quality + 1

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
