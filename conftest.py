import pytest
from main import BooksCollector

@pytest.fixture
def books_collector():
    """Фикстура для создания экземпляра BooksCollector."""
    return BooksCollector()

@pytest.fixture
def sample_books():
    """Фикстура для предоставления списка тестовых книг."""
    return [
        ('1984', 'Драма'),
        ('Ревизор', 'Комедия'),
        ('ОНО', 'Ужасы'),
        ('Гарри Поттер и философский камень', 'Фантастика')
    ]

@pytest.fixture
def setup_books(books_collector, sample_books):
    """Фикстура для добавления тестовых книг в books_collector."""
    for title, genre in sample_books:
        books_collector.add_new_book(title)
        books_collector.set_book_genre(title, genre)
    return books_collector
