import unittest
from app import app

class TestBooks(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_books(self):
        response = self.app.get('/api/books')
        self.assertEqual(response.status_code, 200)

    def test_add_book(self):
        response = self.app.post('/api/books', json={"title": "New Book", "author": "Author Name"})
        self.assertEqual(response.status_code, 201)

    def test_update_book(self):
        response = self.app.put('/api/books/1', json={"available": False})
        self.assertEqual(response.status_code, 200)

    def test_delete_book(self):
        response = self.app.delete('/api/books/1')
        self.assertEqual(response.status_code, 200)
