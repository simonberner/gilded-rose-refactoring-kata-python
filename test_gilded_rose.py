# -*- coding: utf-8 -*-
from gilded_rose import Item, GildedRose


#  Normal item: once the SellIn == 0, Quality degrades twice as fast
def test_normal_item_quality_degrades_twice_as_fast():
    items = [Item("foo", 0, 4)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert 2 == items[0].quality

# More Test Ideas to cover the business rules:
#
# Normal item: at the end of each day the Quality drops by 1
#
# All items: at the end of each day the SellIn drops by 1 (except legendary item Sulfuras)
# All items: The Quality of an item is never negative
# All items: The Quality of an item is never more than 50
#
# Special items:
# "Aged Brie" Quality increases by 1 as long SellIn > 0 days
# "Aged Brie" Quality is never < 0
# "Aged Brie" never decreases in Quality
# "Backstage pass" Quality is never < 0
# "Backstage pass" never decreases in Quality
# "Backstage pass" Quality increases by 1 when SellIn > 10 days
# "Backstage pass" Quality increases by 2 when SellIn <= 10 days
# "Backstage pass" Quality increases by 3 when SellIn <= 5 days
# "Backstage pass" Quality drops to 0 when SellIn == 0 day
#
# Legendary item: "Sulfuras" has a Quality of 80 and never decreases.
# Legendary item: "Sulfuras" SellIn does not change because it never has to be sold

# Questions
# Are there any other "Special Items" in the shop or will be there in the future with some other specific rules to consider??
# Is "Sulfuras" currently the only "Legendary Item" in the shop or will be there more in the future?