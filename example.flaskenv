FLASK_APP=checker.py    # should be left as it is
SECRET_KEY=             # secret key, can be generated via python with command 'python3 -c "print(__import__('secrets').token_hex(32))"'
LOCAL_CURRENCY=         # code of currency you wish to convert to other costs
SYMBOLS=                # comma separated list of currency codes from which it should convert
API_KEY=                # api key which should be taken from https://www.currencyconverterapi.com/

# remove all commentaries before saving this file as '.flaskenv'
