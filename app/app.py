# %% Module Imports
from app.protoclass import addressbook_pb2

# %% Example class declaration
person = addressbook_pb2.Person()
person.id = 1234
person.name = "John Doe"
person.email = "jdoe@example.com"
phone = person.phones.add()
phone.number = "555-4321"
phone.type = addressbook_pb2.Person.HOME

# %% Test incorrect setting of an attribute
person.id = "1"

# %% Test accessing unknown attribute
person.hello = "1"

# %% Example serialization
str(person)

# %%


