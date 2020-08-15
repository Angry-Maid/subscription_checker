import requests
from flask import render_template, redirect, flash, url_for

from app import app, db
from app.forms import AddSubscriptionForm
from app.models import Subscription


@app.route('/')
def index():
    local_currency = app.config['LOCAL_CURRENCY']
    symbols = [symbol for symbol in app.config['SYMBOLS'].split(',') if symbol != local_currency]

    if not app.config['API_KEY']:
        flash('No api key was set in .flaskenv file, go to https://www.currencyconverterapi.com/ for your api key.')
        return render_template(
            'index.html',
            subscriptions=[],
            local_currency=local_currency
        )

    exchange_rates = requests.get(
        'https://free.currconv.com/api/v7/convert',
        params={
            'apiKey': app.config['API_KEY'],
            'q': ','.join([f'{symbol}_{local_currency}' for symbol in symbols]),
            'compact': 'ultra'
        }
    ).json()

    subs = [
        {
            **sub.to_dict(),
            local_currency: sub.cost * exchange_rates[f'{sub.currency}_{local_currency}'] if sub.currency != local_currency else '-'
        } for sub in Subscription.query.order_by(Subscription.billing_date, Subscription.id).all()
    ]

    return render_template(
        'index.html',
        subscriptions=subs,
        local_currency=local_currency,
        total_local=sum(map(lambda x: x[local_currency] if x[local_currency] != '-' else 0, subs))
    )


@app.route('/subscription', methods=['GET', 'POST'])
def subscription():
    form = AddSubscriptionForm()

    if form.validate_on_submit():
        sub = Subscription(
            name=form.name.data,
            cost=form.cost.data,
            currency=form.currency.data,
            billing_date=form.billing_date.data
        )

        db.session.add(sub)
        db.session.commit()

        flash(f'Added \'{form.name.data}\' to subscriptions')
        return redirect(url_for('index'))
    return render_template('subscription.html', form=form)


@app.route('/delete/<_id>')
def delete(_id):
    sub = Subscription.query.filter_by(id=_id).first_or_404()

    flash(f'Deleted \'{sub.name}\' from subscriptions')

    db.session.delete(sub)
    db.session.commit()

    return redirect(url_for('index'))
