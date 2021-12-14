from dataclasses import dataclass


class RegularBook:
    def __init__(self, title, author):
        self.title = title
        self.author = author


@dataclass
class Book:
    title: str
    author: str
