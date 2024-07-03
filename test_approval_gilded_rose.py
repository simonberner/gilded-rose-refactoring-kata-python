from gilded_rose import Item, GildedRose
from approvaltests import verify_all_combinations, Options, DiffReporter
from approvaltests.reporters import PythonNativeReporter


# Checking the following for normal items:
# - sellIn and quality degrades by 1 at the end of each day
# - Once the sell by date has passed, Quality degrades twice as fast
# - The Quality of an item is never negative
# - The Quality of an item is never more than 50
#
# Checking the following for special items:
# - "Aged Brie" actually increases in Quality by 1 the older it gets
# - "Sulfuras", being a legendary item, never has to be sold or decreases in Quality
# - "Sulfuras" is a legendary item and as such its Quality is 80 and it never alters.
# - "Backstage passes", like aged brie, increases in Quality by 1 as its SellIn value approaches;
#   - Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
#   - Quality drops to 0 after the concert
def test_update_sellin_quality():
    verify_all_combinations(
        __do_update_quality,
        [["normal item", "Aged Brie", "Backstage passes to a TAFKAL80ETC concert", "Sulfuras, Hand of Ragnaros"],
         [-1, 0, 5, 6, 10, 11],  # sellIn
         [-1, 0, 4, 50, 51]],  # quality
        options=Options().with_reporter(reporter=PythonNativeReporter())
    )


def __do_update_quality(name, sell_in, quality):
    items = [Item(name, sell_in, quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    item = gilded_rose.items[0]
    return __print_item_as_string(item)


def __print_item_as_string(item):
    return item.name + ", sellIn: " + str(item.sell_in) + ", Quality: " + str(item.quality)
