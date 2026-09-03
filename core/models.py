from dataclasses import dataclass, field
from typing import List, Dict, Any


@dataclass
class Book:
    book_id: str
    title: str
    author: str
    stock: int

    def is_available(self) -> bool:
        return self.stock > 0

    def to_dict(self) -> Dict[str, Any]:
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "stock": self.stock,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Book":
        return cls(**data)


@dataclass
class User:
    user_id: str
    first_name: str
    last_name_paternal: str
    last_name_maternal: str
    borrowed_books: List[str] = field(default_factory=list)

    def can_borrow(self) -> bool:
        return len(self.borrowed_books) < 3

    def to_dict(self) -> Dict[str, Any]:
        return {
            "user_id": self.user_id,
            "first_name": self.first_name,
            "last_name_paternal": self.last_name_paternal,
            "last_name_maternal": self.last_name_maternal,
            "borrowed_books": self.borrowed_books,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "User":
        return cls(**data)
