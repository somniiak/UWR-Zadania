from database import *
from datetime import date
from peewee import DoesNotExist, IntegrityError

init_db()
init_example()

def books_add(author, title, year):
    Book.create(author=author, title=title, year=year)
    return "Book added"


def books_list():
    return [
        f"{b.id}: {b.author} - {b.title} ({b.year})"
        for b in Book.select()
    ]


def books_remove(id):
    try:
        b = Book.get_by_id(id)
        b.delete_instance()
        return "Book deleted"

    except DoesNotExist:
        return "Book not found"


def people_add(name, email):
    try:
        Person.create(name=name, email=email)
        return "Person added"

    except IntegrityError:
        return "Email already exists"


def people_list():
    return [
        f"{p.id}: {p.name} ({p.email})"
        for p in Person.select()
    ]


def people_remove(id):
    try:
        p = Person.get_by_id(id)
        p.delete_instance()
        return "Person deleted"

    except DoesNotExist:
        return "Person not found"


def loans_borrow(book_id, person_id):
    try:
        book = Book.get_by_id(book_id)
        person = Person.get_by_id(person_id)

        active = Loan.select().where(
            (Loan.book == book) & (Loan.return_date.is_null())
        )

        if active.exists():
            return "Book already loaned"

        Loan.create(book=book, person=person)
        return "Book loaned"

    except DoesNotExist:
        return "Book or person not found"


def loans_return(loan_id):
    try:
        loan = Loan.get_by_id(loan_id)

        if loan.return_date:
            return "Book already returned"

        loan.return_date = date.today()
        loan.save()

        return "Book returned"

    except DoesNotExist:
        return "Loan not found"



def loans_delete(id):
    try:
        l = Loan.get_by_id(id)
        l.delete_instance()
        return "Loan deleted"

    except DoesNotExist:
        return "Loan not found"


def loans_list():
    return [
        f"{l.id}: {l.book.title} @ {l.person.name} | "
        f"{'oddana' if l.return_date else 'wypożyczona'}"
        for l in Loan.select()
    ]
