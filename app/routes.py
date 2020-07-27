from flask import render_template, redirect

from app import app
from app.forms import AddSubscription
from app.models import Subscription

@app.route('/')
def index():
    return render_template(
        'index.html', 
        subscriptions=Subscription.query.all()
    )


@app.route('/subscription')
def subscription():
    return 'hello there'
