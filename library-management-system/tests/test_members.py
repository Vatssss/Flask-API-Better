import unittest
from app import app

class TestMembers(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_members(self):
        response = self.app.get('/api/members')
        self.assertEqual(response.status_code, 200)

    def test_add_member(self):
        response = self.app.post('/api/members', json={"name": "New Member", "email": "member@example.com"})
        self.assertEqual(response.status_code, 201)

    def test_update_member(self):
        response = self.app.put('/api/members/1', json={"name": "Updated Name", "email": "updated@example.com"})
        self.assertEqual(response.status_code, 200)

    def test_delete_member(self):
        response = self.app.delete('/api/members/1')
        self.assertEqual(response.status_code, 200)
