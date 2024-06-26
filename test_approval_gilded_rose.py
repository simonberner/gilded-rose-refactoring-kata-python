from gilded_rose import Item, GildedRose
from approvaltests import verify


# Check that sellIn and Quality degrades by 1 for a normal item
def test_update_quality():
    items = [Item("normal item", 10, 4)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    item = gilded_rose.items[0]
    item_as_string = __print_item_as_string(item)
    verify(item_as_string)


def __print_item_as_string(item):
    return item.name + ", sellIn: " + str(item.sell_in) + ", Quality: " + str(item.quality)
