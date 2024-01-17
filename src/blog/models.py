import datetime


from mongoengine import Document, EmbeddedDocument, ListField, EmbeddedDocumentField, DateTimeField, StringField, \
    IntField


class Blog(EmbeddedDocument):
    name = StringField(max_length=255)
    text = StringField()
    author = StringField(max_length=255)
    rating = IntField(defauit=100)

    def __str__(self):
        return f"{self.name}"


class Entity(Document):
    blog = ListField(EmbeddedDocumentField(Blog))
    timestamp = DateTimeField(default=datetime.datetime.now())
    headline = StringField(max_lenght=255)

    def __str__(self):
        return f"{self.headline}"
