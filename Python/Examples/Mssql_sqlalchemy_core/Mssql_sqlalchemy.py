"""
Sqlalchemy Core examples.

The below follows through the tutorial at:
https://docs.sqlalchemy.org/en/latest/core/tutorial.html
"""

# ============
# Imports
# ============
# create_engine - Used to specify which database to connect to.
#                 In this tutorial, it will be a new one in memory.
# MetaData      - Used to get information on the database
# The rest are used below in 'Creating tables'
from sqlalchemy import (create_engine, Table, Column,
                        Integer, String, MetaData, ForeignKey)


# ============
# Creating an engine instance
# ============
eng = create_engine('sqlite:///:memory:', echo=True)
# echo=True     Sets up logging

# ============
# Creating tables
# ============
# Creating a "Users" we can interact with.
metadata = MetaData()
users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String(50)),
              Column('fullname', String(50)))

addresses = Table('addresses', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('user_id', None, ForeignKey('users.id')),
                  Column('email_address', String(50), nullable=False))

# Now to actually create the tables we've specified above
metadata.create_all(eng)
