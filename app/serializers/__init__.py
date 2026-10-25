"""Concrete serializer implementations - following SRP and OCP."""

import json
import xml.etree.ElementTree as ET

from app.domain.book import Book
from app.interfaces import BookSerializer


class JSONBookSerializer(BookSerializer):
    """Serialize book to JSON format."""
    
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLBookSerializer(BookSerializer):
    """Serialize book to XML format."""
    
    def serialize(self, book: Book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")