# -*- coding: utf-8 -*-
from gilded_rose import Item, GildedRose


# The Quality of an item is never negative
def test_item_quality_not_negative():
    items = [Item("Bread", -1, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality == 0


# Once the sell by date has passed, Quality degrades twice as fast
def test_item_quality_decreases_twice_as_fast_after_sell_by_date():
    items = [Item("Jam", 0, 10)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality == 8


# At the end of each day our system lowers SellIn and Quality for every item
def test_item_quality_decreases_each_day():
    items = [Item("Cheese", 5, 10)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality == 9
    assert gilded_rose.items[0].sell_in == 4


# "Aged Brie" actually increases in Quality the older it gets
# (Here the quality increases twice as fast because the sell by date has passed)
def test_aged_brie_increases_in_quality():
    items = [Item("Aged Brie", 0, 10)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality == 12
    assert gilded_rose.items[0].sell_in == -1


# "Sulfuras", being a legendary item, never has to be sold or decreases in Quality
# (As it never has to be sold, the SellIn does not decrease)
def test_sulfuras_never_changes_quality():
    items = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality == 80
    assert gilded_rose.items[0].sell_in == 5


# The Quality of an item is never more than 50
def test_item_quality_never_more_than_50():
    items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 50)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality == 50
    assert gilded_rose.items[0].sell_in == 4


# Backstage passes (or aged Brie): Quality increases by 2 when there are 10 days or less
def test_backstage_passes_quality_increases_by_2_when_10_days_or_less():
    items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality == 22
    assert gilded_rose.items[0].sell_in == 9


# Backstage passes (or aged Brie): Quality increases by 3 when there are 5 days or less
def test_backstage_passes_quality_increases_by_3_when_5_days_or_less():
    items = [Item("Backstage passes to a TAFKAL80ETC concert", 1, 20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality == 23
    assert gilded_rose.items[0].sell_in == 0


# Backstage passes (or aged Brie): Quality drops to 0 after the concert (when SellIn < 1)
def test_backstage_passes_quality_drops_to_0_after_concert():
    items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality == 0
    assert gilded_rose.items[0].sell_in == -1
