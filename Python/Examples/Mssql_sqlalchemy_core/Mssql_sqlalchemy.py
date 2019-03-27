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
from sqlalchemy.sql import select


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

# ============
# Shortening the insert to make it simpler.
# ============
ins = users.insert()
conn.execute(ins, id=2, name="test", fullname="test2")

# ============
# Execute many (works with insert(), update(), and delete()
# ============
# When inserting many items into a db, a 'LIST of DICTS' can be supplied.
# An example below:
ins = addresses.insert()
list_of_dicts = [
    {'user_id': 1, 'email_address': 'testemail1@gmail.com'},
    {'user_id': 1, 'email_address': 'testemail2@gmail.com'},
    {'user_id': 2, 'email_address': 'testemail3@gmail.com'},
    {'user_id': 2, 'email_address': 'testemail4@gmail.com'}
]
conn.execute(ins, list_of_dicts)

# ============
# Selecting
# ============
s = select([users])
result = conn.execute(s)
print("-----------")
for row in result:
    print(row)
result.close()  # always close it
# Prints a tuple like result:
# (1, 'test', 'Test Name')
# (2, 'test', 'test2')
print("-----------")

# You can also access the results similar to a dictionary.
result = conn.execute(s)
for row in result:
    print('test')
result.close()  # always close it
print("-----------")

# Can also use column objects directly.
for row in conn.execute(s):
    print("name:", row[users.c.name], "; fullname:", row[users.c.fullname])
# name: test ; fullname: Test Name
# name: test ; fullname: test2
print("-----------")