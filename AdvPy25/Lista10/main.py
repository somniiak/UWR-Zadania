from parser import parser
from database import *
from datetime import date
from peewee import DoesNotExist

init_db()
init_example()
args = parser.parse_args()

if args.type == "book":
    if args.action == "add":
        Book.create(author=args.author, title=args.title, year=args.year)
        print("Dodano książkę.")

    elif args.action == "list":
        for b in Book.select():
            print(f"{b.id}: {b.author} - {b.title} ({b.year})")

elif args.type == "person":
    if args.action == "add":
        Person.create(name=args.name, email=args.email)
        print("Dodano osobę.")

    elif args.action == "list":
        for p in Person.select():
            print(f"{p.id}: {p.name} ({p.email})")

elif args.type == "loan":
    if args.action == "borrow":
        try:
            book = Book.get_by_id(args.book_id)
            person = Person.get_by_id(args.person_id)

            active = Loan.select().where(
                (Loan.book == book) & (Loan.return_date.is_null())
            )

            if active.exists():
                print("Książka jest już wypożyczona.")
            else:
                Loan.create(book=book, person=person)
                print("Wypożyczono książkę.")

        except DoesNotExist:
            print("Nieprawidłowe dane.")

    elif args.action == "return":
        try:
            loan = Loan.get_by_id(args.loan_id)
            loan.return_date = date.today()
            loan.save()
            print("Książka zwrócona.")

        except DoesNotExist:
            print("Nieprawidłowe dane.")

    elif args.action == "list":
        for l in Loan.select():
            status = "oddana" if l.return_date else "wypożyczona"
            print(f"{l.id}: {l.book.title} @ {l.person.name} | {status}")
