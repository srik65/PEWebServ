
class Config(object):
  SQLALCHEMY_DATABASE_URI = 'sqlite://'
  SQLALCHEMY_TRACK_MODIFICATIONS = False

  PERSON_DATA_FIELDS =  [
    "first_name",
    "last_name",
    "age",
    "favourite_colour",
    "nationality"
  ]
