from app import db


class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), index=True)
    cost = db.Column(db.Float)
    currency = db.Column(db.String(32))
    billing_date = db.Column(db.Integer)
    active = db.Column(db.Boolean)

    def __repr__(self):
        return '<Subscription {}:{}>'.format(self.id, self.name)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'cost': self.cost,
            'currency': self.currency,
            'billing_date': self.billing_date,
            'active': self.active
        }
