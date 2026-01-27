from argparse import ArgumentParser

parser = ArgumentParser(description="Program przechowujący informacje o posiadanych książkach.")
parser.add_argument("--mode", choices=["local", "api"], required=True)

sub = parser.add_subparsers(dest="type", required=True)

# Książki
books_parser = sub.add_parser("books", help="Operacje na książkach")
books_sub = books_parser.add_subparsers(dest="action", required=True)

books_add = books_sub.add_parser("add", help="Dodaj nową książkę")
books_add.add_argument("--author", type=str, required=True)
books_add.add_argument("--title", type=str, required=True)
books_add.add_argument("--year", type=int, required=True)

books_list = books_sub.add_parser("list", help="Lista wszystkich zapisanych książek")


# Osoby
people_parser = sub.add_parser("people", help="Operacje na osobach")
people_sub = people_parser.add_subparsers(dest="action", required=True)

people_add = people_sub.add_parser("add", help="Dodaj dane przyjaciela")
people_add.add_argument("--name", type=str, required=True)
people_add.add_argument("--email", type=str, required=True)

people_list = people_sub.add_parser("list", help="Lista wszystkich dodanych przyjaciół")


# Wypożyczenia
loans_parser = sub.add_parser("loans", help="Wypożyczenia")
loans_sub = loans_parser.add_subparsers(dest="action", required=True)

loans_borrow = loans_sub.add_parser("borrow", help="Wypożycz książkę")
loans_borrow.add_argument("--book-id", type=int, required=True)
loans_borrow.add_argument("--person-id", type=int, required=True)

loans_return = loans_sub.add_parser("return", help="Zwróć książkę")
loans_return.add_argument("--loan-id", type=int, required=True)

loans_list = loans_sub.add_parser("list", help="Lista wszystkich wypożyczeń")