"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE = 'https://tinyurl.com/demo-cupcake'

def connect_db(app):
    app.app_context().push()
    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    """model for cupcake"""

    __tablename__ = "cupcakes"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True,
                   nullable=False)
    flavor = db.Column(db.Text,
                       nullable=False)
    size = db.Column(db.Text,
                     nullable=False)
    rating = db.Column(db.Float,
                       nullable=False)
    image = db.Column(db.Text,
                      nullable=False,
                      default=DEFAULT_IMAGE)
    
    def to_dict(self):
        """return serialized version of cupcake info"""

        return {
            "id": self.id,
            "flavor": self.flavor,
            "size": self.size,
            "rating": self.rating,
            "image": self.image,
        }