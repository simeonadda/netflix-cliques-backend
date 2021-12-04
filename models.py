import os
from playhouse.db_url import connect
from peewee import *
from flask_login import UserMixin

if 'ON_HEROKU' in os.environ:

    DATABASE = connect(os.environ.get('DATABASE_URL'))
    # Connect to the database URL defined in the environment, falling
    # back to a local Sqlite database if no database URL is specified.

else:
    DATABASE = SqliteDatabase('nfclx.sqlite')


# USER MODEL
class User(UserMixin, Model):
    name = CharField()
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()
    confirm_password = CharField()

    class Meta:
        database = DATABASE


# CLIQUE MODEL
class Clique(Model):
    name = CharField()
    owner = ForeignKeyField(User, backref='cliques')
    members = IntegerField()

    class Meta:
        database = DATABASE


# NETFLIX TITLE MODEL
class Title(Model):
    image = CharField()
    title = CharField()
    titleDetails = CharField()
    filmId = IntegerField()

    class Meta:
        database = DATABASE



def initialize():
    DATABASE.connect()

    # DATABASE.drop_tables([User])
    DATABASE.create_tables([User, Clique, Title], safe=True)
    print("Connected on the DB and created tables if they don't already exist 🎉")

    DATABASE.close()
