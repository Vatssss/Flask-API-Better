from flask import Blueprint, jsonify, request
from models import books

books_bp = Blueprint('books', __name__)

# GET: List all books
@books_bp.route('/books', methods=['GET'])
def get_books():
    return jsonify(books), 200

# POST: Add a new book
@books_bp.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = {
        "id": len(books) + 1,
        "title": data['title'],
        "author": data['author'],
        "available": True
    }
    books.append(new_book)
    return jsonify(new_book), 201

# PUT: Update a book's availability
@books_bp.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    for book in books:
        if book['id'] == book_id:
            book['available'] = data['available']
            return jsonify(book), 200
    return jsonify({"message": "Book not found"}), 404

# DELETE: Remove a book
@books_bp.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return jsonify({"message": "Book deleted successfully"}), 200
