from argparse import ArgumentParser

parser = ArgumentParser(description="Program przechowujący informacje o posiadanych książkach.")

sub = parser.add_subparsers(dest="type", required=True)

# Książki
book_parser = sub.add_parser("book", help="Operacje na książkach")
book_sub = book_parser.add_subparsers(dest="action", required=True)

book_add = book_sub.add_parser("add", help="Dodaj nową książkę")
book_add.add_argument("--author", type=str, required=True)
book_add.add_argument("--title", type=str, required=True)
book_add.add_argument("--year", type=int, required=True)

book_list = book_sub.add_parser("list", help="Lista wszystkich zapisanych książek")


# Osoby
person_parser = sub.add_parser("person", help="Operacje na osobach")
person_sub = person_parser.add_subparsers(dest="action", required=True)

person_add = person_sub.add_parser("add", help="Dodaj dane przyjaciela")
person_add.add_argument("--name", type=str, required=True)
person_add.add_argument("--email", type=str, required=True)

person_list = person_sub.add_parser("list", help="Lista wszystkich dodanych przyjaciół")


# Wypożyczenia
loan_parser = sub.add_parser("loan", help="Wypożyczenia")
loan_sub = loan_parser.add_subparsers(dest="action", required=True)

loan_borrow = loan_sub.add_parser("borrow", help="Wypożycz książkę")
loan_borrow.add_argument("--book-id", type=int, required=True)
loan_borrow.add_argument("--person-id", type=int, required=True)

loan_return = loan_sub.add_parser("return", help="Zwróć książkę")
loan_return.add_argument("--loan-id", type=int, required=True)

loan_list = loan_sub.add_parser("list", help="Lista wszystkich wypożyczeń")