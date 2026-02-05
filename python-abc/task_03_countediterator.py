#!/usr/bin/env python3


class CountedIterator:
    """Class to iterate over a sequence and count items."""

    def __init__(self, data):
        """Initialize the iterator from data and set counter to zero."""
        self.iterator = iter(data)
        self.counter = 0

    def get_count(self):
        """Return the current value of the counter."""
        return self.counter

    def __next__(self):
        """Fetch next item, increment counter and return item."""
        item = next(self.iterator)
        self.counter += 1
        return item

    def __iter__(self):
        """Return the iterator object itself to allow loop usage."""
        return self
