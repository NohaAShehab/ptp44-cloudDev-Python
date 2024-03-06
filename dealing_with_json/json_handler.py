import json


def read_all_data(file_name):
    try:
        fileobject = open(file_name, 'r')
        data = json.load(fileobject)  # read string --> inform of
        # python  datatypes
        # data= fileobject.read()
    except Exception as e :
        print(e)
        return []
    else:
        return  data


# def save_book(book, file_name):
#     try:
#         fileobject = open(file_name, 'a')
#         # fileobject.write(str(book))
#         json.dump(book, fileobject)
#     except Exception as e :
#         print(e)
#         return False
#     else:
#         return  True


def save_book(book, file_name):
    old_books = read_all_data(file_name)  # list
    old_books.append(book)  # add to the list
    try:
        fileobject = open(file_name, 'w')  # remove old data
        json.dump(old_books, fileobject, indent=4)
    except Exception as e :
        print(e)
        return False
    else:
        return  True

