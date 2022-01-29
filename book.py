from dataclasses import dataclass


@dataclass
class Book:
    isbn: str
    title: str
    authors: list
    description: str
    language: str
    year: int

