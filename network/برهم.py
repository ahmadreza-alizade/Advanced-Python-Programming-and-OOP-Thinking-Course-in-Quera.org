import requests
# from requests import get


def has_it(name, category, url):
    response = requests.get(url).json()
    if len(list(response)) != 0:
        for item in response:
            if name == item["name"]:
                return (True)
    return (False)


def add_book(name, category, url):
    my_data = {'name': name, 'category': category}
    target = requests.post(url, data=my_data)
    if target.status_code == 200:
        return (False)
    return (True)


def process(book):
    math_url = "http://127.0.0.1:8000/math/"
    physic_url = "http://127.0.0.1:8000/physic/"
    chess_url = "http://127.0.0.1:8000/chess/"

    name_book = book["name"]
    category_book = book["category"]

    if category_book == "math":
        if has_it(name_book, category_book, math_url):
            return ("bad query")
        elif add_book(name_book, category_book, math_url):
            return ("bad query")

    if category_book == "physic":
        if has_it(name_book, category_book, physic_url):
            return ("bad query")
        elif add_book(name_book, category_book, physic_url):
            return ("bad query")

    if category_book == "chess":
        if has_it(name_book, category_book, chess_url):
            return ("bad query")
        elif add_book(name_book, category_book, chess_url):
            return ("bad query")
