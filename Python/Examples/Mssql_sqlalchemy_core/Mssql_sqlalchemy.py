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
print('--------')

# ============
# Inserting into tables
# ============
ins = users.insert()
print(ins)
# Prints INSERT INTO users (id, name, fullname) VALUES (:id, :name, :fullname)

ins = users.insert().values(name='test', fullname='Test Name')
print(ins)
# Prints INSERT INTO users (name, fullname) VALUES (:name, :fullname)
# Notice it still only shows the placeholders for the insert values
# To see the actual values, use the below:
print(ins.compile().params)

# To actually execute the query (insert).
# To do that, we need to set up a connection.
conn = eng.connect()

# "The Connection object represents an actively checked out
# DBAPI connection resource."

# Now you can send it the insert statement we'e set up.
result = conn.execute(ins)
