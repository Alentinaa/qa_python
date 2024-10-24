from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_add_book_with_59_symbols_in_name(self, books_collector):
        books_collector.add_new_book('Книга с очень длинным названием, которое больше 40 символов')
        assert len(books_collector.get_books_genre()) == 0

    def test_set_book_genre_correct_genre(self, books_collector):
        books_collector.add_new_book('Автостопом по галактике')
        books_collector.set_book_genre('Автостопом по галактике', 'Фантастика')
        assert books_collector.get_book_genre('Автостопом по галактике') == 'Фантастика'

    def test_set_book_genre_inexistent_genre(self, books_collector):
        books_collector.add_new_book('Преступление и наказание')
        books_collector.set_book_genre('Преступление и наказание', 'Роман')
        assert books_collector.get_book_genre('Преступление и наказание') == ''

    def test_get_book_genre_by_exist_name(self, books_collector):
        books_collector.add_new_book('ОНО')
        books_collector.set_book_genre('ОНО', 'Ужасы')
        assert books_collector.get_book_genre('ОНО') == 'Ужасы'

    def test_get_books_with_specific_genre_comedy(self, books_collector):
        books_collector.add_new_book('Ревизор')
        books_collector.add_new_book('Горе от ума')
        books_collector.add_new_book('Трое в лодке, не считая собаки')

        books_collector.set_book_genre ('Ревизор','Комедия')
        books_collector.set_book_genre ('Горе от ума', 'Комедия')
        books_collector.set_book_genre ('Трое в лодке, не считая собаки', 'Комедия')

        assert books_collector.get_books_with_specific_genre('Комедия') == [
            'Ревизор',
            'Горе от ума',
            'Трое в лодке, не считая собаки'
        ]

    def test_get_books_genre_empty_list(self, books_collector):
        books_collector.add_new_book('Книга без жанра')
        assert books_collector.get_books_genre() == {}

    def test_get_books_for_children_return_books_with_age_rating(self, books_collector):
        books_collector.add_new_book('Гарри Поттер и философский камень')
        books_collector.add_new_book('Винни Пух и все-все-все')

        books_collector.set_book_genre('Гарри Поттер и философский камень', 'Фэнтези')
        books_collector.set_book_genre('Винни Пух и все-все-все', 'Мультфильм')

        assert books_collector.get_books_for_children() == ['Гарри Поттер и философский камень', 'Винни Пух и все-все-все']

    def test_add_book_in_favorites_valid_added(self, books_collector):
        books_collector.add_new_book('1984')
        books_collector.add_book_in_favorites('1984')
        assert '1984' in books_collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_not_existing_book(self, books_collector):
        books_collector.add_book_in_favorites('Неизвестная книга')
        assert 'Неизвестная книга' not in books_collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_exist_book(self, books_collector):
        books_collector.add_new_book('1984')
        books_collector.add_book_in_favorites('1984')
        books_collector.delete_book_from_favorites('1984')
        assert '1984' not in books_collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_book_not_in_favorites(self, books_collector):
        books_collector.add_new_book('ОНО')
        books_collector.delete_book_from_favorites('ОНО')
        assert 'ОНО' not in books_collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_valid_option(self, books_collector):
        books_collector.add_new_book('Ревизор')
        books_collector.add_book_in_favorites('Ревизор')
        favorites = books_collector.get_list_of_favorites_books()
        assert favorites == ['Ревизор']

