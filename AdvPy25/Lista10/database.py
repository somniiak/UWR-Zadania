from peewee import *
from datetime import date
import json

db = SqliteDatabase("data.db")


class BaseModel(Model):
    class Meta:
        database = db


class Book(BaseModel):
    author = CharField(constraints=[Check("length(author) > 0")])
    title = CharField(constraints=[Check("length(title) > 0")])
    year = IntegerField(constraints=[Check("year > 0")])


class Person(BaseModel):
    name = CharField(constraints=[Check("length(name) > 0")])
    email = CharField(unique=True)


class Loan(BaseModel):
    book = ForeignKeyField(Book, on_delete="CASCADE")
    person = ForeignKeyField(Person, on_delete="CASCADE")
    loan_date = DateField(default=date.today())
    return_date = DateField(null=True)


def init_db():
    db.connect()
    db.create_tables([Book, Person, Loan])


def init_example(json_file="sample.json"):
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    for book in data.get("books", []):
        if not Book.select().where(Book.title == book["title"]).exists():
            Book.create(**book)

    for person in data.get("people", []):
        if not Person.select().where(Person.email == person["email"]).exists():
            Person.create(**person)
