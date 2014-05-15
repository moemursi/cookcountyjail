"""

models.py

Database models

See:
https://docs.google.com/drawings/d/1WAXGB1l5QcX_2XV5_VjvVNNxOO9UvGIh5jXgakNnICo/

"""

from ccj.app import db

"""
Base Models

"""

class Person(db.Model):
    """
    A person model used to identify people who
    are in the jail and stores general
    information.

    We don't track first or last names.

    """
    id = db.Column(db.Integer, primary_key=True)

    # a hash to uniquely identify the person
    # if he or she came back to the jail
    hash = db.Column(db.Unicode(64), unique=True, nullable=False)

    # gender can only be M(male) or F(female)
    gender = db.Column(db.Enum("M", "F", name="pgender"))

    # race would be harder to parse with an
    # enum so we are sticking to good old
    # strings
    race = db.Column(db.Unicode(4))

    # the date this person was added to the
    # database
    date_created = db.Column(db.Date)

class ChargeDescription(db.Model):
    """
    Every inmate gets a charge when they are
    booked. Often this changes overtime for
    some reason.

    """

    id = db.Column(db.Integer, primary_key=True)

    # the charge will have a description
    description = db.Column(db.Unicode, nullable=False, unique=True)

    date_created = db.Column(db.Date)

class Statute(db.Model):
    """
    A statute.

    """

    id = db.Column(db.Integer, primary_key=True)

    citation = db.Column(db.Unicode, nullable=False, unique=True)

    date_created = db.Column(db.Date)

class Housing(db.Model):
    """
    This model represents a place where
    an inmate is housed during his stay
    at the jail.

    """
    id = db.Column(db.Integer, primary_key=True)

    # the entire housing location without
    # any alterations
    location = db.Column(db.Unicode)

    # the inmates are housed in different
    # divisions
    division = db.Column(db.Unicode)

    # a way to specify where in a division the
    # inmate is located
    sub_division = db.Column(db.Unicode)

    # and an even further specific location
    # in the division
    sub_division_location = db.Column(db.Unicode)

    date_created = db.Column(db.Date)

    # some location represent inmates who
    # aren't really housed in the jail
    # for example when being under Day Release
    in_jail = db.Column(db.Boolean)

    # some inmates are in special programs
    # that can be deducted based on their
    # housing location
    in_program = db.Column(db.Unicode)

class CourtBuilding(db.Model):
    """
    A court building where an inmate goes to trial.

    """

    id = db.Column(db.Integer, primary_key=True)

    text = db.Column(db.Unicode)

    name = db.Column(db.Unicode)

    branch = db.Column(db.Unicode)

    address = db.Column(db.Unicode)

    city = db.Column(db.Unicode)

    state = db.Column(db.Unicode)

    zip = db.Column(db.Unicode)

    date_created = db.Column(db.Date)

class CourtRoom(db.Model):
    """
    The court room in a court building
    where an inmate is trialed.

    """
    id = db.Column(db.Integer, primary_key=True)

    # the court room's number
    number = db.Column(db.Integer)

    court_building_id = db.Column(db.Integer, db.ForeignKey('court_building.id'))

    court_building = db.relationship('CourtBuilding',
        backref=db.backref('court_rooms', lazy='dynamic'))


    date_created = db.Column(db.Date)

