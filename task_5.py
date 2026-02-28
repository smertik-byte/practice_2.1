import json
import os

FILENAME = 'resourse/library.json'
EXPORT_FILENAME = 'resourse/library_export.txt'

initial_books = [
    {
        "id": 1,
        "title": "Мастер и Маргарита",
        "author": "Булгаков",
        "year": 1967,
        "available": True,
    },
    {
        "id": 2,
        "title": "Преступление и наказание",
        "author": "Достоевский",
        "year": 1866,
        "available": False,
    },
]


def load_books():
    if not os.path.exists(FILENAME):
        with open(FILENAME, 'w', encoding='utf-8') as file:
            json.dump(initial_books, file, ensure_ascii=False, indent=4)
    with open(FILENAME, 'r', encoding='utf-8') as file:
        return json.load(file)


def save_books(books):
    with open(FILENAME, 'w', encoding='utf-8') as file:
        json.dump(books, file, ensure_ascii=False, indent=4)


def display_books(books):
    if not books:
        print('Библиотека пуста.')
        return
    print('\nСписок книг:')
    for book in books:
        status = 'Доступна' if book['available'] else 'Недоступна'
        print(
            f"ID: {book['id']}, Название: {book['title']}, "
            f"Автор: {book['author']}, Год: {book['year']}, Статус: {status}"
        )


def search_books(books):
    term = input('Введите название или автора для поиска: ').lower()
    results = [
        book for book in books
        if term in book['title'].lower() or term in book['author'].lower()
    ]
    if results:
        display_books(results)
    else:
        print('Ничего не найдено.')


def add_book(books):
    try:
        new_id = max([book['id'] for book in books], default=0) + 1
        title = input('Введите название книги: ')
        author = input('Введите автора: ')
        year = int(input('Введите год издания: '))
        new_book = {
            'id': new_id,
            'title': title,
            'author': author,
            'year': year,
            'available': True,
        }
        books.append(new_book)
        save_books(books)
        print('Книга добавлена.')
    except ValueError:
        print('Некорректный ввод. Год должен быть числом.')


def change_status(books):
    try:
        book_id = int(input('Введите ID книги: '))
        for book in books:
            if book['id'] == book_id:
                book['available'] = not book['available']
                save_books(books)
                status = 'Доступна' if book['available'] else 'Недоступна'
                print(f'Статус книги изменен на: {status}')
                return
        print('Книга с таким ID не найдена.')
    except ValueError:
        print('Некорректный ввод ID.')


def delete_book(books):
    try:
        book_id = int(input('Введите ID книги для удаления: '))
        for i, book in enumerate(books):
            if book['id'] == book_id:
                del books[i]
                save_books(books)
                print('Книга удалена.')
                return
        print('Книга с таким ID не найдена.')
    except ValueError:
        print('Некорректный ввод ID.')


def export_available_books(books):
    available_books = [b for b in books if b['available']]
    with open(EXPORT_FILENAME, 'w', encoding='utf-8') as file:
        for b in available_books:
            file.write(
                f"ID: {b['id']}, Название: {b['title']}, "
                f"Автор: {b['author']}, Год: {b['year']}\n"
            )
    print('Доступные книги экспортированы в "{EXPORT_FILENAME}".')


def main():
    books = load_books()
    while True:
        print('\nМеню:')
        print('1. Просмотр всех книг')
        print('2. Поиск по автору/названию')
        print('3. Добавление новой книги')
        print('4. Изменение статуса книги (выдача/возврат)')
        print('5. Удаление книги по ID')
        print('6. Экспорт доступных книг')
        print('0. Выход')
        choice = input('Выберите действие: ')

        if choice == '1':
            display_books(books)
        elif choice == '2':
            search_books(books)
        elif choice == '3':
            add_book(books)
        elif choice == '4':
            change_status(books)
        elif choice == '5':
            delete_book(books)
        elif choice == '6':
            export_available_books(books)
        elif choice == '0':
            print('До свидания!')
            break
        else:
            print('Некорректный выбор. Попробуйте снова.')


if __name__ == '__main__':
    main()