

"""
    book_store:
        book : id , title, price

"""
from book_handler import (display_all_books,
    create_book)

def mainmenu():
    while True:
        choice = input("please enter your choice: ")
        if choice == "c":
            create_book()
        elif choice == "e":
            pass
        elif choice == "d":
            pass
        elif choice == "l":
            book=display_all_books()
            # return book
        elif choice=='x':
            exit()
        else:
            print("--- wrong choice  please try again---")

if __name__ == "__main__":
    book=mainmenu()