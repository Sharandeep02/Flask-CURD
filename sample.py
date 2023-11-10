from flask import Flask, request, jsonify

app = Flask(__name__)

books = [
    {'id': 1, 'title': 'Book1', 'author': "Author 1", },
    {'id': 2, 'title': 'Book2', 'author': "Author 2", },
    {'id': 3, 'title': 'Book3', 'author': "Author 3"}
]


@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({"Books": books})


@app.route('/books/<int:book_id>', methods=['GET', 'PUT'])
def get_book(book_id):
    if request.method == 'GET':
        for book in books:
            if book['id'] == book_id:
                return book
        return {'error': 'book not found'}
    if request.method == 'PUT':
        for book in books:
            if book['id'] == book_id:
                book['title'] = request.json['title']
                book['author'] = request.json['author']
                print()
                return book
        return {'error': 'book not found'}


@app.route('/books', methods=['POST'])
def create_book():
    new_book = {'id': len(books) + 1, 'title': request.json['title'], 'author': request.json['author']}
    books.append(new_book)
    return new_book


"""@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    for book in books:
        if book['id'] == book_id:
            book['title'] = request.json['title']
            book['author'] = request.json['author']
            return book
    return {'error': 'book not found'}"""


@app.route('/books/<int:book_id>', methods=['DELETE'])
def del_book(book_id):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return {"Data": "Book deleted successfully"}

    return {"error": "Book id not found"}


if __name__ == '__main__':
    app.run(debug=True, port=8081)
