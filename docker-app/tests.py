import unittest
from flask import Flask, jsonify
from app import app, db
from app.models import Person

test_client = app.test_client()

class RouterTestCase(unittest.TestCase):

  def setUp(self):
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
    db.create_all()

  def tearDown(self):
    db.session.remove()
    db.drop_all()

  def test_create_person(self):
    with app.app_context():
      response = test_client.post('/persons', json={
          'first_name': 'Srikanth', 'last_name': 'Yachamaneni', 'age': 28, 'nationality': "Indian", 'favourite_colour': 'red'
      })
      self.assertEqual(response.status_code, 200)
      self.assertEqual(response.get_json()['first_name'], 'Srikanth')
      self.assertEqual(response.get_json()['last_name'], 'Yachamaneni')
      self.assertEqual(response.get_json()['age'], 28)
      self.assertEqual(response.get_json()['favourite_colour'], 'red')

  def test_update_person(self):
    with app.app_context():
      #CREATE
      response = test_client.post('/persons', json={
          'first_name': 'Srikanth', 'last_name': 'Yachamaneni', 'age': 28, 'nationality': "Indian", 'favourite_colour': 'red'
      })
      #UPDATE
      response = test_client.put('/persons/1', json={
          'first_name': 'Srihari', 'last_name': 'Yachamaneni', 'age': 31, 'nationality': "Indian", 'favourite_colour': 'green'
      })
      #COMPARE
      self.assertEqual(response.status_code, 200)
      self.assertEqual(response.get_json()['first_name'], 'Srihari')
      self.assertEqual(response.get_json()['last_name'], 'Yachamaneni')
      self.assertEqual(response.get_json()['age'], 31)
      self.assertEqual(response.get_json()['favourite_colour'], 'green')

  def test_delete_person(self):
    with app.app_context():
      #CREATE
      response = test_client.post('/persons', json={
          'first_name': 'Srikanth', 'last_name': 'Yachamaneni', 'age': 28, 'nationality': "Indian", 'favourite_colour': 'red'
      })
      self.assertEqual(response.status_code, 200)
      #DELETE
      response = test_client.post('/persons/1/delete')
      self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main(verbosity=2)
