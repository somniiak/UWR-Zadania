from database import *
from datetime import date
from peewee import DoesNotExist, IntegrityError
from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

# (C)reate - PUT
# (R)ead - GET
# (U)pdate - POST
# (D)elet - DELETE

class BookReq(Resource):
    def get(self, id):
        try:
            b = Book.get_by_id(id)
            return {
                "id": b.id,
                "author": b.author,
                "title": b.title,
                "year": b.year,
            }

        except DoesNotExist:
            return {"error": "Book not found"}, 404
    
    def post(self, id):
        try:
            b = Book.get_by_id(id)
            data = request.json

            b.author = data.get('author', b.author)
            b.title = data.get('title', b.title)

            if "year" in data:
                try:
                    b.year = int(data["year"])
                except (ValueError, TypeError):
                    return {"error": "Book year must be an integer"}, 400

            b.save()
            return {"msg": "Book updated"}

        except DoesNotExist:
            return {"error": "Book not found"}, 404

    def delete(self, id):
        try:
            b = Book.get_by_id(id)
            b.delete_instance()
            return {"msg": "Book deleted"}

        except DoesNotExist:
            return {"error": "Book not found"}, 404


class BookList(Resource):
    def get(self):
        return [
            {
                "id": b.id,
                "author": b.author,
                "title": b.title,
                "year": b.year,
            }
            for b in Book.select()
        ]

    def put(self):
        data = request.json

        if not data:
            return {"error": "Missing request body"}, 400

        if "author" not in data:
            return {"error": "Missing book author"}, 400

        if "title" not in data:
            return {"error": "Missing book title"}, 400

        if "year" not in data:
            return {"error": "Missing book year"}, 400

        try:
            year = int(data["year"])
        
        except (ValueError, TypeError):
            return {"error": "Book year must be an integer"}, 400
        
        if year <= 0:
            return {"error": "Book year must be positive"}, 400

        Book.create(
            author=data['author'],
            title=data['title'],
            year=year,
        )

        return {"msg": "Book added"}, 201


class PersonReq(Resource):
    def get(self, id):
        try:
            p = Person.get_by_id(id)
            return {
                "id": p.id,
                "name": p.name,
                "email": p.email
            }

        except DoesNotExist:
            return {"error": "Person not found"}, 404
    
    def post(self, id):
        try:
            p = Person.get_by_id(id)
            data = request.json

            p.name = data.get('name', p.name)
            p.email = data.get('email', p.email)

            try:
                p.save()

            except IntegrityError:
                return {"error": "Email already exists"}, 409

            return {"msg": "Person updated"}

        except DoesNotExist:
            return {"error": "Person not found"}, 404

    def delete(self, id):
        try:
            p = Person.get_by_id(id)
            p.delete_instance()
            return {"msg": "Person deleted"}

        except DoesNotExist:
            return {"error": "Person not found"}, 404


class PersonList(Resource):
    def get(self):
        return [
            {
                "id": p.id,
                "name": p.name,
                "email": p.email,
            }
            for p in Person.select()
        ]

    def put(self):
        data = request.json

        if not data:
            return {"error": "Missing request body"}, 400

        if "name" not in data:
            return {"error": "Missing person's name"}, 400

        if "email" not in data:
            return {"error": "Missing person's email"}, 400

        try:
            Person.create(
                name=data['name'],
                email=data['email'],
            )

        except IntegrityError:
            return {"error": "Email already exists"}, 409

        return {"msg": "Person added"}, 201


class LoanReq(Resource):
    def get(self, id):
        try:
            l = Loan.get_by_id(id)
            return {
                "id": l.id,
                "book": l.book.title,
                "person": l.person.name,
                "returned": l.return_date.isoformat() if l.return_date else None
            }

        except DoesNotExist:
            return {"error": "Loan not found"}, 404
    
    def post(self, id):
        try:
            loan = Loan.get_by_id(id)

            if loan.return_date:
                return {"error": "Book already returned"}, 409

            loan.return_date = date.today()
            loan.save()
            return {"msg": "Book returned"}

        except DoesNotExist:
            return {"error": "Loan not found"}, 404


    def delete(self, id):
        try:
            loan = Loan.get_by_id(id)
            loan.delete_instance()
            return {"msg": "Loan deleted"}

        except DoesNotExist:
            return {"error": "Loan not found"}, 404



class LoanList(Resource):
    def get(self):
        return [
            {
                "id": l.id,
                "book": l.book.title,
                "person": l.person.name,
                "returned": l.return_date.isoformat() if l.return_date else None
            }
            for l in Loan.select()
        ]

    def put(self):
        data = request.json

        if not data:
            return {"error": "Missing request body"}, 400

        if "book_id" not in data:
            return {"error": "Missing book_id"}, 400

        if "person_id" not in data:
            return {"error": "Missing person_id"}, 400

        try:
            book_id = int(data["book_id"])
            book = Book.get_by_id(book_id)

            person_id = int(data["person_id"])
            person = Person.get_by_id(person_id)

        except (ValueError, TypeError):
            return {"error": "book_id and person_id must be integers"}, 400

        except DoesNotExist:
            return {"error": "Book or person not found"}, 404

        active = Loan.select().where(
                (Loan.book == book) & (Loan.return_date.is_null())
        )

        if active.exists():
            return {"error": "Book already loaned"}, 409

        Loan.create(
            book=book,
            person=person
        )

        return {"msg": "Book loaned"}, 201


api.add_resource(BookReq, "/books/<int:id>")
api.add_resource(BookList, "/books")

api.add_resource(PersonReq, "/people/<int:id>")
api.add_resource(PersonList, "/people")

api.add_resource(LoanReq, "/loans/<int:id>")
api.add_resource(LoanList, "/loans")

if __name__ == "__main__":
    app.run(debug=True)