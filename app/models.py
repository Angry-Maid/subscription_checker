from app import db


class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), index=True)
    cost = db.Column(db.Float)
    currency = db.Column(db.String(32))
    billing_date = db.Column(db.Integer)

    def __repr__(self):
        return '<Subscription {};{}>'.format(self.id, self.name)
