#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        if not isinstance(size, int):
            print("size must be an integer")
            return
        self.brand = brand
        self.size = size
        self.condition = 'New'

    def repair(self):
        print("The shoe has been repaired.")
        self.condition = 'New'

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = 'New'
    pass