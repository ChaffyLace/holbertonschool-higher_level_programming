#!/usr/bin/env python3


class SwimMixin:
    """class for swimming capability."""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """class for flying capability."""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Class representing a dragon."""

    def roar(self):
        print("The dragon roars!")
