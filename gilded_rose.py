# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:

            # Decrease day
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1

            # Decrease the quality of normal item
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert" and item.name != "Sulfuras, Hand of Ragnaros":
                if item.quality > 0:
                    item.quality = item.quality - 1
            # Increase quality for special items
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1

            # Once the sell by date has passed, Quality degrades twice as fast (meaning an additional decrease of -1)
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.name != "Sulfuras, Hand of Ragnaros" and item.quality > 0:
                            # Decrease quality
                            item.quality = item.quality - 1
                    # Quality drops to 0 after the concert
                    else:
                        item.quality = 0
                else:
                    if item.quality < 50:
                        # Increase quality
                        item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
