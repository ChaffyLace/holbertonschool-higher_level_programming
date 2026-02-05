#!/usr/bin/env python3
"""Module task_02_verboselist."""


class VerboseList(list):
    """Custom list class with notification messages."""

    def append(self, item):
        """Add item to list and print message."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, items):
        """Extend list with items and print message."""
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """Remove item from list and print message."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pop item from list and print message."""
        print("Popped [{}] from the list.".format(self[index]))
        return super().pop(index)
