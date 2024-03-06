from json_handler import read_all_data, save_book
import time

def generate_id():
    return round(time.time())
def display_all_books():
    books = read_all_data("books.json")
    print(books)
    return books


def create_book():
    title = input("Enter book title: ")
    price = input("Enter book price: ")
    id = generate_id()
    book_details = {
        "title":title,
        "price":price,
        "id":id
    }
    print(book_details)
    save_book(book_details, "books.json")