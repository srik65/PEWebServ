from app import app
from flask import jsonify
from flask import request
from app.models import Person
from app import db
from app.errors import bad_request
from config import Config

@app.route('/persons/<int:id>', methods=['GET'])
def get_person(id):
  return jsonify(Person.query.get_or_404(id).to_dict())

@app.route('/persons', methods=['GET'])
@app.route('/persons/', methods=['GET'])
def get_persons():
  return jsonify(Person.to_collection_dict(Person.query.all()))

@app.route('/persons', methods=['POST'])
def create_person():
  data = request.get_json() or {}
  # fields = ['first_name','last_name', 'age', 'favourite_color', 'nationality']
  for elem in Config.PERSON_DATA_FIELDS:
    if elem not in data:
      return bad_request('must include ' + str(Config.PERSON_DATA_FIELDS))
  person = Person()
  person.from_dict(data)
  db.session.add(person)
  db.session.commit()
  app.logger.info("created person: "+str(person))
  response = jsonify(person.to_dict())
  response.response_code = 201
  return response

@app.route('/persons/<int:id>', methods=['PUT'])
def update_person(id):
  person = Person.query.get_or_404(id)
  data = request.get_json() or {}
  if 'first_name' in data and data['first_name'] != person.first_name and \
            Person.query.filter_by(first_name=data['first_name']).first():
        return bad_request('please use a different first_name')
  person.from_dict(data)
  db.session.commit()
  return jsonify(person.to_dict())

@app.route('/persons/<int:id>/delete', methods=['POST'])
def delete_person(id):
  person = Person.query.get_or_404(id)
  db.session.delete(person)
  db.session.commit()
  app.logger.info("deleted person with id: "+str(id))
  return jsonify(person.to_dict())

