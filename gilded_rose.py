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

        if is_aged_brie:
            if not is_sulfuras:  # SMELL: repeated conditional
                self.sell_in = self.sell_in - 1
                if self.quality < 50:
                    self.quality = self.quality + 1
                    if is_backstage_pass:
                        if self.sell_in < 11:
                            if self.quality < 50:
                                self.quality = self.quality + 1
                        if self.sell_in < 6:
                            if self.quality < 50:
                                self.quality = self.quality + 1
            # Once the sell by date has passed, Quality degrades twice as fast (meaning an additional decrease of -1)
            if self.sell_in < 0:
                if self.quality < 50:
                    # Increase quality
                    self.quality = self.quality + 1
        else:
            if not is_sulfuras:  # SMELL: repeated conditional
                self.sell_in = self.sell_in - 1
            # Decrease the quality of normal item
            if not is_backstage_pass and not is_sulfuras:  # SMELL: repeated conditional
                if self.quality > 0:
                    self.quality = self.quality - 1
            # Increase quality for special items
            else:
                if self.quality < 50:
                    self.quality = self.quality + 1
                    if is_backstage_pass:
                        if self.sell_in < 11:
                            if self.quality < 50:
                                self.quality = self.quality + 1
                        if self.sell_in < 6:
                            if self.quality < 50:
                                self.quality = self.quality + 1
            # Once the sell by date has passed, Quality degrades twice as fast (meaning an additional decrease of -1)
            if self.sell_in < 0:
                if not is_backstage_pass:
                    if not is_sulfuras and self.quality > 0:
                        # Decrease quality
                        self.quality = self.quality - 1
                    # Quality drops to 0 after the concert for Backstage passes
                else:
                    self.quality = 0


def __repr__(self):
    return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
