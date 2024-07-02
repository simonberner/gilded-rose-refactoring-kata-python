from gilded_rose import Item, GildedRose
from approvaltests import verify_all_combinations, Options, DiffReporter
from approvaltests.reporters import PythonNativeReporter


# Check that sellIn and Quality degrades by 1 for a normal item
def test_update_quality():
    verify_all_combinations(
        do_update_quality,
        [["normal item", "Aged Brie", "Backstage passes to a TAFKAL80ETC concert", "Sulfuras, Hand of Ragnaros"],
         [10],  # sellIn
         [4]],  # quality
        options=Options().with_reporter(reporter=PythonNativeReporter())
    )


def do_update_quality(name, sell_in, quality):
    items = [Item(name, sell_in, quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    item = gilded_rose.items[0]
    return __print_item_as_string(item)


def __print_item_as_string(item):
    return item.name + ", sellIn: " + str(item.sell_in) + ", Quality: " + str(item.quality)
