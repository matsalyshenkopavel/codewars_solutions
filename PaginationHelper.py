"""For this exercise you will be strengthening your page-fu mastery. You will complete the PaginationHelper class,
which is a utility class helpful for querying paging information related to an array.
The class is designed to take in an array of values and an integer indicating how many items will be allowed per each page.
The types of values contained within the collection/array are not relevant."""


# TODO: complete this class

from math import ceil

class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.pageitems = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        return ceil(self.item_count() / self.pageitems)


    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index < 0 or page_index >= self.page_count():
            return -1
        elif page_index < (self.page_count() - 1):
            return self.pageitems
        else:
            return self.pageitems if self.item_count() % self.pageitems == 0 else self.item_count() % self.pageitems
    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index < 0 or item_index > (self.item_count() - 1):
            return -1
        else:
            return (item_index // self.pageitems)
