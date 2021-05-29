class Books():
  def __init__(self) -> None:
      self.books = {}
      self.number = 0

  def add_book(self, book):
    self.number += 1
    self.books[self.number] = book

  def __str__(self) -> str:
      return str(self.books)


class StoreBooks():
  @staticmethod
  def save_books(filename, books):
    with open(filename, "w") as f:
      f.write(str(books))


x = Books()
x.add_book("qwerty")
print(x)

s = StoreBooks()
s.save_books("book_store.txt", x)
