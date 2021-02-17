from itertools import zip_longest

import requests
from flask import render_template, redirect, flash, url_for, request

from app import app, db
from app.forms import SubscriptionForm
from app.models import Subscription


def grouper(n, it, fill=None):
    args = [iter(it)] * n
    return zip_longest(fillvalue=fill, *args)


@app.route('/')
def index():
    local_currency = lc = app.config['LOCAL_CURRENCY']
    symbols = [
        symbol for symbol in app.config['SYMBOLS'].split(',')
        if symbol != local_currency
    ]

    if not app.config['API_KEY']:
        flash(
            'No api key was set in .flaskenv file, '
            'go to https://www.currencyconverterapi.com/ for your api key.'
        )
        return render_template(
            'index.html',
            subscriptions=[],
            local_currency=local_currency
        )

    exchange_rates = {}
    for items in grouper(2, symbols):
        exchange_rates.update(
            requests.get(
                'https://free.currconv.com/api/v7/convert',
                params={
                    'apiKey': app.config['API_KEY'],
                    'q': ','.join(
                        [
                            f'{symbol}_{local_currency}'
                            for symbol in filter(None.__ne__, items)
                        ]
                    ),
                    'compact': 'ultra'
                }
            ).json()
        )

    subs = [
        {
            **sub.to_dict(),
            local_currency: sub.cost * exchange_rates[f'{sub.currency}_{lc}']
            if sub.currency != local_currency else '-'
        } for sub in
        Subscription.query.order_by(
            Subscription.billing_date, Subscription.id
        ).all()
    ]

    return render_template(
        'index.html',
        subscriptions=subs,
        local_currency=local_currency,
        total_local=sum(
            map(
                lambda x:
                    y if (y := x[local_currency]) != '-' and
                    x['active'] else 0,
                subs
            )
        )
    )


@app.route('/subscription', methods=['GET', 'POST'])
def subscription():
    form = SubscriptionForm()

    if form.validate_on_submit():
        sub = Subscription(
            name=form.name.data,
            cost=form.cost.data,
            currency=form.currency.data,
            billing_date=form.billing_date.data,
            active=True
        )

        db.session.add(sub)
        db.session.commit()

        flash(f'Added \'{form.name.data}\' to subscriptions')
        return redirect(url_for('index'))
    return render_template('subscription.html', form=form, action='Create')


@app.route('/delete/<_id>')
def delete(_id):
    sub = Subscription.query.filter_by(id=_id).first_or_404()

    flash(f'Deleted \'{sub.name}\' from subscriptions')

    db.session.delete(sub)
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/active/<_id>')
def switch_active(_id):
    sub = Subscription.query.filter_by(id=_id).first_or_404()

    flash(f'Updated active status on \'{sub.name}\'')

    sub.active = not sub.active

    db.session.commit()

    return redirect(url_for('index'))


@app.route('/edit/<_id>', methods=['GET', 'POST'])
def edit(_id):
    sub = Subscription.query.filter_by(id=_id).first_or_404()

    if request.method == 'GET':
        form = SubscriptionForm(obj=sub)
    else:
        form = SubscriptionForm()
        form.populate_obj(sub)

        db.session.commit()

        return redirect(url_for('index'))

    return render_template('subscription.html', form=form, action='Edit')
