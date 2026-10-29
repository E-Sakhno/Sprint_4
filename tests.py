from main import BooksCollector
from data import prepared_books
import pytest


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    @pytest.mark.parametrize("name", prepared_books)
    def test_add_new_book_with_less_or_equal_40_symbols_is_in_collector(self, book_collector, name):
        book_collector.add_new_book(name)
        assert name in book_collector.books_genre

    @pytest.mark.parametrize("name", prepared_books)
    def test_add_new_book_twice_only_one_in_collector(self, book_collector, name):
        book_collector.add_new_book(name)
        book_collector.add_new_book(name)
        assert len(book_collector.books_genre) == 1

    @pytest.mark.parametrize("name, genre", [["1984", "Фантастика"], ["Женьба Фигаро", "Комедии"]])
    def test_get_book_genre_returns_genre_for_existing_book(self, book_collector, name, genre):
        book_collector.add_new_book(name)
        book_collector.set_book_genre(name, genre)
        assert book_collector.get_book_genre(name) == genre

    def test_get_book_genre_from_invalid_genre_keeps_empty_genre(self, book_collector):
        book_collector.add_new_book("Колобок")
        book_collector.set_book_genre("Колобок", "Детская сказка")
        assert book_collector.get_book_genre("Колобок") == ""

    @pytest.mark.parametrize("genre, count", [["Ужасы", 1], ["Мультфильмы", 2], ["Фантастическая комедия", 0]])
    def test_get_books_with_specific_genre_count_genres(self, book_collector, genre, count):
        book_collector.add_new_book("Гордость и предубеждение и зомби")
        book_collector.set_book_genre("Гордость и предубеждение и зомби", "Ужасы")
        book_collector.add_new_book("Что делать, если ваш кот хочет вас убить")
        book_collector.set_book_genre("Что делать, если ваш кот хочет вас убить", "Детективы")
        book_collector.add_new_book("Колобок")
        book_collector.set_book_genre("Колобок", "Мультфильмы")
        book_collector.add_new_book("Винни Пух")
        book_collector.set_book_genre("Винни Пух", "Мультфильмы")
        assert len(book_collector.get_books_with_specific_genre(genre)) == count

    @pytest.mark.parametrize(
        "name, genre",
        [
            ["Гордость и предубеждение и зомби", "Ужасы"],
            ["Что делать, если ваш кот хочет вас убить", "Детективы"],
            ["1984", "Фантастика"],
            ["Колобок", "Мультфильмы"],
            ["Женитьба Фигаро", "Комедии"],
        ],
    )
    def test_get_books_genre_is_not_empty(self, book_collector, name, genre):
        book_collector.add_new_book(name)
        book_collector.set_book_genre(name, genre)
        assert len(book_collector.get_books_genre()) != 0

    @pytest.mark.parametrize(
        "name, genre",
        [
            ["Гордость и предубеждение и зомби", "Ужасы"],
            ["Что делать, если ваш кот хочет вас убить", "Детективы"],
        ],
    )
    def test_get_books_for_children_adult_books_not_in_array(self, book_collector, name, genre):
        book_collector.add_new_book(name)
        book_collector.set_book_genre(name, genre)
        assert name not in book_collector.get_books_for_children()

    @pytest.mark.parametrize(
            "name, genre",
            [
                ["Колобок", "Мультфильмы"],
                ["Через тернии - к звездам", "Фантастика"],
                ["Женитьба Фигаро", "Комедии"],
            ],
        )
    def test_get_books_for_children_children_books_in_array(self, book_collector, name, genre):
        book_collector.add_new_book(name)
        book_collector.set_book_genre(name, genre)
        assert name in book_collector.get_books_for_children()    

    @pytest.mark.parametrize("name", prepared_books)
    def test_add_book_in_favorites_book_in_array(self, book_collector, name):
        book_collector.add_new_book(name)
        book_collector.add_book_in_favorites(name)
        assert book_collector.favorites == [name]

    @pytest.mark.parametrize("name", prepared_books)
    def test_get_list_of_favorites_books_book_in_array(self, book_collector, name):
        book_collector.add_new_book(name)
        book_collector.add_book_in_favorites(name)
        assert len(book_collector.get_list_of_favorites_books()) == 1

    @pytest.mark.parametrize("name", prepared_books)
    def test_delete_book_from_favorites_removes_book(self, book_collector, name):
        book_collector.add_new_book(name)
        book_collector.add_book_in_favorites(name)
        book_collector.delete_book_from_favorites(name)
        assert len(book_collector.favorites) == 0
