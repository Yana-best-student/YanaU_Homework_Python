from book import Book

library = [
    Book("Война и мир", "Лев Толстой"),
    Book("Евгений Онегин", "Александр Пушкин"),
    Book("Мастер и Маргарита", "Михаил Булгаков")
]

for book in library:
    print(f"{book.title} - {book.author}")