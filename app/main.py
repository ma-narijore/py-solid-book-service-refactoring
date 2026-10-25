import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod


class Type(ABC):

    @abstractmethod
    def display(self) -> None:
        pass

    @abstractmethod
    def print_book(self) -> None:
        pass


class SerializeType(ABC):
    @abstractmethod
    def serialize(self) -> str:
        pass

class Book:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content


#                 BOOKVIEWS
class BookViewConsole(Book, Type):
    def display(self) -> None:

        try:
            print(self.content)
        except:
            # raise ValueError(f"Unknown display type: {display_type}")
            raise ValueError(f"Unknown error")

    def print_book(self) -> None:
        try:
            print(f"Printing the book: {self.title}...")
            print(self.content)

        except:
            raise ValueError(f"Unknown print type:")


class BookViewReverse(Book, Type):

    def display(self) -> None:
        try:
            print(self.content[::-1])
        except:
            raise ValueError(f"Unknown display type:")

    def print_book(self) -> None:
        try:
            print(f"Printing the book in reverse: {self.title}...")
            print(self.content[::-1])

        except:
            raise ValueError(f"Unknown print type:")


#           SERIALIZERS
class JSONBook(Book, SerializeType):
    def serialize(self) -> str:
        try:
            return json.dumps({"title": self.title, "content": self.content})

        except:
            raise ValueError(f"Unknown serialize type:")


class XMLBook(Book, SerializeType):
    def serialize(self) -> str:
        try:
            root = ET.Element("book")
            title = ET.SubElement(root, "title")
            title.text = self.title
            content = ET.SubElement(root, "content")
            content.text = self.content

            return ET.tostring(root, encoding="unicode")
        except:
            raise ValueError(f"Unknown serialize type: ")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:

    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                BookViewConsole(book.title, book.content).display()

            elif method_type == "reverse":
                BookViewReverse(book.title, book.content).display()

        elif cmd == "print":
            if method_type == "console":
                BookViewConsole(book.title, book.content).print_book()

            elif method_type == "reverse":
                BookViewReverse(book.title, book.content).print_book()

        elif cmd == "serialize":
            if method_type == "xml":
                return XMLBook(book.title, book.content).serialize()

            elif method_type == "json":
                return JSONBook(book.title, book.content).serialize()


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
