# qa_python

`test_add_new_book_with_less_or_equal_40_symbols_is_in_collector` — проверяет, что в коллектор успешно добавляется книга с именем длиной 40 символов или меньше

`test_add_new_book_twice_only_one_in_collector` — проверяет, что при повторном добавлении одной и той же книги в словаре `books_genre` остаётся только одна запись

`test_set_book_genre_adds_valid_genre_for_exist_book` — проверяет, что метод `set_book_genre` устанавливает книге жанр из списка доступных жанров, и он сохраняется в словаре `books_genre`

`test_get_book_genre_returns_genre_for_existing_book` — проверяет, что для существующей книги с установленным жанром метод `get_book_genre` возвращает этот жанр

`test_get_book_genre_from_invalid_genre_keeps_empty_genre` — проверяет, что при попытке установить книге жанр, которого нет в списке доступных, жанр остаётся пустой строкой

`test_get_books_with_specific_genre_count_genres` — проверяет, что метод `get_books_with_specific_genre` возвращает корректное количество книг для заданного жанра, включая случай жанра, отсутствующего в списке доступных (возвращается 0)

`test_get_books_genre_is_not_empty` — проверяет, что метод `get_books_genre` возвращает непустой словарь после добавления книги и установки ей жанра

`test_get_books_for_children_adult_books_not_in_array` — проверяет, что книги с жанрами, имеющими возрастной рейтинг (`Ужасы`, `Детективы`), не попадают в список книг для детей

`test_get_books_for_children_children_books_in_array` — проверяет, что книги с жанрами без возрастного рейтинга (`Мультфильмы`, `Фантастика`, `Комедии`) попадают в список книг для детей

`test_add_book_in_favorites_book_in_array` — проверяет, что книга, находящаяся в словаре `books_genre`, успешно добавляется в список избранного

`test_get_list_of_favorites_books_book_in_array` — проверяет, что метод `get_list_of_favorites_books` возвращает список из одной добавленной в избранное книги

`test_delete_book_from_favorites_removes_book` — проверяет, что книга, находящаяся в избранном, успешно удаляется из списка `favorites`