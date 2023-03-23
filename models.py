# models.py


from datetime import datetime

from config import db


class Person(db.Model):

    __tablename__ = "person"

    id = db.Column(db.Integer, primary_key=True)

    lname = db.Column(db.String(32), unique=True)

    fname = db.Column(db.String(32))

    timestamp = db.Column(

        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow

    )
    
    

class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        load_instance = True
        sqla_session = db.session

person_schema = PersonSchema()
people_schema = PersonSchema(many=True)


"""
    Line 3 imports the datetime object from the datetime module that comes with Python. This gives you a way to create a timestamp in the Person class in lines 11 to 13.
    Line 4 imports db, an instance of SQLAlchemy that you defined in the config.py module. This gives models.py access to SQLAlchemy attributes and methods.
    Line 6 defines the Person class. Inheriting from db.Model gives Person the SQLAlchemy features to connect to the database and access its tables.
    Line 7 connects the class definition to the person database table.
    Line 8 declares the id column containing an integer acting as the primary key for the table.
    Line 9 defines the last name field with a string value. This field must be unique because you’re using lname as the identifier for a person in a REST API URL.
    Line 10 defines the first name field with a string value.
    Lines 11 to 13 define a timestamp field with a datetime value.
"""
