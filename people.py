# people.py


#from datetime import datetime (removed to make way for adjustments in part 2)
from flask import abort
from flask import abort, make_response

from config import db


def get_timestamp():

    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

""" (removed to make adjustments for part 2)
PEOPLE = {

    "Fairy": {

        "fname": "Tooth",

        "lname": "Fairy",

        "timestamp": get_timestamp(),

    },

    "Ruprecht": {

        "fname": "Knecht",

        "lname": "Ruprecht",

        "timestamp": get_timestamp(),

    },

    "Bunny": {

        "fname": "Easter",

        "lname": "Bunny",

        "timestamp": get_timestamp(),

    }

}"""



def read_all(): #new read_all from part 2
    people = Person.query.all()
    return people_schema.dump(people)


#def read_all():

#    return list(PEOPLE.values())
    
    
def create(person): #creates person obj, related to POST operation in yml file

    lname = person.get("lname")

    fname = person.get("fname", "")


    if lname and lname not in PEOPLE:

        PEOPLE[lname] = {

            "lname": lname,

            "fname": fname,

            "timestamp": get_timestamp(),

        }

        return PEOPLE[lname], 201

    else:

        abort(

            406,

            f"Person with last name {lname} already exists",

        )

def read_one(lname):
    person = Person.query.filter(Person.lname == lname).one_or_none()

    if person is not None:
        return person_schema.dump(person)
    else:
        abort(404, f"Person with last name {lname} not found")

def create(person):
    lname = person.get("lname")
    existing_person = Person.query.filter(Person.lname == lname).one_or_none()

    if existing_person is None:
        new_person = person_schema.load(person, session=db.session)
        db.session.add(new_person)
        db.session.commit()
        return person_schema.dump(new_person), 201
    else:
        abort(406, f"Person with last name {lname} already exists")

def update(lname, person):
    existing_person = Person.query.filter(Person.lname == lname).one_or_none()

    if existing_person:
        update_person = person_schema.load(person, session=db.session)
        existing_person.fname = update_person.fname
        db.session.merge(existing_person)
        db.session.commit()
        return person_schema.dump(existing_person), 201
    else:
        abort(404, f"Person with last name {lname} not found")

def delete(lname):
    existing_person = Person.query.filter(Person.lname == lname).one_or_none()

    if existing_person:
        db.session.delete(existing_person)
        db.session.commit()
        return make_response(f"{lname} successfully deleted", 200)
    else:
        abort(404, f"Person with last name {lname} not found")

        
"""      (old form prior to p2)
def read_one(lname): #returns data if last name found by Flask app, related to GET operation in yml file
    if lname in PEOPLE:
        return PEOPLE[lname]
    else:
        abort(
            404, f"Person with last name {lname} not found"
        )
        
      (old form prior to p2)   
def update(lname, person): #updates person obj, related to PUT operation in yml file
    if lname in PEOPLE:
        PEOPLE[lname]["fname"] = person.get("fname", PEOPLE[lname]["fname"])
        PEOPLE[lname]["timestamp"] = get_timestamp()
        return PEOPLE[lname]
    else:
        abort(
            404,
            f"Person with last name {lname} not found"
        )

 (old form prior to p2)
def delete(lname): #removes person obj, related to DELETE operation in yml file
    if lname in PEOPLE:
        del PEOPLE[lname]
        return make_response(
            f"{lname} successfully deleted", 200
        )
    else:
        abort(
            404,
            f"Person with last name {lname} not found"
        ) """


