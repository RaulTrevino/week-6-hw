from app import db
from datetime import datetime

class BarModel(db.Model):

  __tablename__ = 'bars'

  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String, nullable = False)
  address = db.Column(db.String, nullable = False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
  type = db.Column(db.String, nullable = False)

  def __repr__(self):
    return f'<Bars: {self.name}>'
  
  def save(self):
    db.session.add(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()