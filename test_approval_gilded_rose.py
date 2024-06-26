from gilded_rose import Item, GildedRose
from approvaltests import verify


# Check that sellIn and Quality degrades by 1 for a normal item
def test_update_quality():
    name = "normal item"
    sellIn = 10
    quality = 4

    item_as_string = do_update_quality(name, quality, sellIn)
    verify(item_as_string)


def do_update_quality(name, quality, sellIn):
    items = [Item(name, sellIn, quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    item = gilded_rose.items[0]
    return __print_item_as_string(item)


def __print_item_as_string(item):
    return item.name + ", sellIn: " + str(item.sell_in) + ", Quality: " + str(item.quality)
