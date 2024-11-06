# TODO Найдите количество книг, которое можно разместить на дискете

data = 1.44 * 1024 * 1024
pages = 100
rows = 50
sym = 25
data_symbol = 4

size_book = pages * rows * sym * data_symbol

number_books = data // size_book

print("Количество книг, помещающихся на дискету:", int(number_books))
