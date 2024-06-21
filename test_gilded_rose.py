# -*- coding: utf-8 -*-
from gilded_rose import Item, GildedRose


#  Normal item: once the SellIn == 0, Quality degrades twice as fast
def test_normal_item_quality_degrades_twice_as_fast():
    items = [Item("foo", 0, 4)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert 2 == items[0].quality
