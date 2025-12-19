from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# Naming convention for Alembic migrations
metadata = MetaData()

# Create the SQLAlchemy extension
db = SQLAlchemy(metadata=metadata)


# Define a model class
class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)

    def __repr__(self):
        return f"<Pet id={self.id} name={self.name} species={self.species}>"
