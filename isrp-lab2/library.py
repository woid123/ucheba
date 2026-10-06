books = []


def add_book(title, author):
    books.append({"title": title, "author": author})


def find_by_author(author):
    return [b for b in books if b["author"] == author]


def count_books():
    """Возвращает число книг в библиотеке."""
    return f"В библиотеке {len(books)} книг(и)"


def remove_book(title):
    for b in books:
        if b["title"] == title:
            books.remove(b)
            return True
    return False
