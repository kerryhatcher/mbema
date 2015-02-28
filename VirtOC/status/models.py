__author__ = 'kwhatcher'


from mongoengine import *


class Status(Document):
    status = StringField(max_length=120, required=True)
    date = IntField(required=True)
