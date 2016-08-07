"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.
>>> Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
>>> Model.query.filter_by(name='Corvette', brand_name='Chevrolet').all()

# Get all models that are older than 1960.
>>> db.session.query(Model).filter(Model.year > 1960).all()
    # or db.session.query(Model.name)

# Get all brands that were founded after 1920.
>>> db.session.query(Brand).filter(Brand.founded > 1920).all()
    # or db.session.query(Brand.name)

# Get all models with names that begin with "Cor".
>>> Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
>>> db.session.query(Brand).filter(Brand.founded == 1903, Brand.discontinued== None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
>>> db.session.query(Brand).filter(db.or_(Brand.discontinued.isnot(None), Brand.founded < 1950)).all()

    #### QUESTION - Why can't I do this? I've been struggling to use the pipe for OR

    #>>> Brand.query.filter((Brand.discontinued.isnot(None)|Brand.founded < 1950)).all()

# Get any model whose brand_name is not Chevrolet.
>>> db.session.query(Model).filter(Model.brand_name != 'Chevrolet').all()

# Fill in the following functions. (See directions for more info.)


def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    # not sure if I should put an actual 'year' value to output anything
    print db.session.query(Model.name, Model.brand_name, Brand.headquarters).filter(Model.year == year).all()


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    print db.session.query(Model.brand_name, Model.name).order_by(Model.brand_name).all()


# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

    ### ANSWER:
    # Return value: <flask_sqlalchemy.BaseQuery object at 0x7fc0aa9aa910>

    # Datatype: It is a query object. If we want to return a Brand object we need to include .all() .first() .one() or .get() with our query.
        # Question - would our Brand object be a 'results' object?


# 2. In your own words, what is an association table, and what *type* of relationship does an association table manage?

    ### ANSWER:
    # An association table does not have any new value, rather it is another table that helps 'glue' the fields between two different tables. It acts like a middle table to create 2 one to many relatinoships.
    # An association table manages many to many relationships.

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):

    return db.session.query(Brand).filter(db.or_(Brand.name.like('%'+mystr+'%'), Brand.name == mystr)).all()


def get_models_between(start_year, end_year):

    return db.session.query(Model).filter(Model.year < end_year, Model.year > start_year).all()
