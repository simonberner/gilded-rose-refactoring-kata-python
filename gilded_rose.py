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

        # Handling Aged Brie
        if is_aged_brie:
            self.calculate_quality_aged_brie()
        else:
            if not is_sulfuras:
                self.sell_in = self.sell_in - 1
            # Decrease the quality of normal item
            if not is_backstage_pass and not is_sulfuras:
                if self.quality > 0:
                    self.quality = self.quality - 1
            else:
                if self.quality < 50:
                    self.quality = self.quality + 1
                    if is_backstage_pass:
                        self.increase_quality_backstage_pass()
            # Once the sell by date has passed, Quality degrades twice as fast (meaning an additional decrease of -1)
            if self.sell_in < 0:
                self.calc_quality_sellin_reached(is_backstage_pass, is_sulfuras)

    def calc_quality_sellin_reached(self, is_backstage_pass, is_sulfuras):
        if is_backstage_pass:
            self.quality = 0  # Quality drops to 0 after the concert for Backstage passes
        else:
            if not is_sulfuras and self.quality > 0:
                # Decrease quality
                self.quality = self.quality - 1

    def increase_quality_backstage_pass(self):
        if self.quality < 50 and self.sell_in < 11:
            self.quality = self.quality + 1
        if self.sell_in < 6:
            self.quality = self.quality + 1

    def calculate_quality_aged_brie(self):
        self.sell_in = self.sell_in - 1
        if self.quality < 50:
            self.quality = self.quality + 1
        # Once the sell by date has passed, Quality degrades twice as fast (meaning an additional decrease of -1)
        if self.sell_in < 0:
            if self.quality < 50:
                # Increase quality
                self.quality = self.quality + 1


def __repr__(self):
    return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
