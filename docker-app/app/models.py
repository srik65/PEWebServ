from app import db
from config import Config

class Person(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  age = db.Column(db.Integer, index=True, unique=False)
  first_name = db.Column(db.String(128), index=True, unique=True)
  last_name = db.Column(db.String(128), index=True, unique=False)
  nationality = db.Column(db.String(128), index=True, unique=False)
  favourite_colour = db.Column(db.String(128), index=True, unique=False)

  def __repr__(self):
    return '<Person {}>'.format(self.first_name)

  def to_dict(self):
    data = {
        'id': self.id,
        'first_name': self.first_name,
        'last_name':  self.last_name,
        # 'nationality': self.nationality,
        'favourite_colour': self.favourite_colour,
        'age':  self.age
    }
    return data

  def from_dict(self, data):
    for field in Config.PERSON_DATA_FIELDS:
      if field in data:
        setattr(self, field, data[field])

  @staticmethod
  def to_collection_dict(items):
    return {"person":[item.to_dict() for item in items]}


