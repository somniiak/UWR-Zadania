import requests

BASE_URL = "http://127.0.0.1:5000"


def books_add(author, title, year):
    r = requests.put(
        f"{BASE_URL}/books",
        json={
            "author": author,
            "title": title,
            "year": year
        }
    )

    if r.status_code == 201:
        return r.json().get("msg")
    return r.json().get("error")


def books_list():
    r = requests.get(f"{BASE_URL}/books")
    r.raise_for_status()

    return [
        f"{b['id']}: {b['author']} - {b['title']} ({b['year']})"
        for b in r.json()
    ]


def books_remove(id):
    r = requests.delete(f"{BASE_URL}/books/{id}")

    if r.status_code == 404:
        return "Book not found"
    return r.json().get("msg", "Book deleted")


def people_add(name, email):
    r = requests.put(
        f"{BASE_URL}/people",
        json={
            "name": name,
            "email": email
        }
    )

    if r.status_code == 201:
        return r.json().get("msg")
    return r.json().get("error")


def people_list():
    r = requests.get(f"{BASE_URL}/people")
    r.raise_for_status()

    return [
        f"{p['id']}: {p['name']} ({p['email']})"
        for p in r.json()
    ]


def people_remove(id):
    r = requests.delete(f"{BASE_URL}/people/{id}")

    if r.status_code == 404:
        return "Person not found"
    return r.json().get("msg", "Person deleted")


def loans_borrow(book_id, person_id):
    r = requests.put(
        f"{BASE_URL}/loans",
        json={
            "book_id": book_id,
            "person_id": person_id
        }
    )

    if r.status_code == 201:
        return r.json().get("msg")
    return r.json().get("error")


def loans_return(loan_id):
    r = requests.post(f"{BASE_URL}/loans/{loan_id}")

    if r.status_code == 200:
        return r.json().get("msg")
    return r.json().get("error")


def loans_delete(id):
    r = requests.delete(f"{BASE_URL}/loans/{id}")

    if r.status_code == 404:
        return "Loan not found"
    return r.json().get("msg", "Loan deleted")


def loans_list():
    r = requests.get(f"{BASE_URL}/loans")
    r.raise_for_status()

    return [
        f"{l['id']}: {l['book']} @ {l['person']} | "
        f"{'oddana' if l['returned'] else 'wypożyczona'}"
        for l in r.json()
    ]
