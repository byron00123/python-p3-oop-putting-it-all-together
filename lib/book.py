#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        if not isinstance(page_count, int):
            print("page_count must be an integer")
            return
        self.title = title
        self.page_count = page_count

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")


if __name__ == "__main__":
    book = Book("Sample Book", "100")
    book.turn_page()
    pass
    
        