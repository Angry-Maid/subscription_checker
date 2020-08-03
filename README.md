# Subscription checker

A simple flask application written as a side project for my convenience.
Most of what this application does is allows us to add services we subscribed to for tracking when and what amount of money will be subtracted monthly.

Additional feature is that we can customize which currencies we are using and which currencies services use to bill us.

This project was done with help of first four chapters of [Miguel's Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

Current list of features(done/not done):
- [x] Add service
- [x] Convert currencies to local currency
- [ ] Edit added services
- [ ] Delete added services

## Installation
First steps is ensuring you have right versions of python, at least 3.6+ for `secrets` std-library (not necessary)

Steps:
1. Cloning this repo:
    ```bash
    $ git clone $repo_url
    ```
2. Creating enviroment and installing requirements
    ```bash
    $ python3 -mvenv venv
    $ source venv/scripts/activate
    (venv) $ python3 -mpip install -r req.txt --user
    ```
3. Editing `example.flaskenv` file and generating secret key
    ```bash
    (venv) $ python3 -c "print(__import__('secrets').token_hex(32))"
    ```
4. Applying existing migrations to create database (sqlite3)
   ```bash
   (venv) $ flask db upgrade
   ```
5. Running the application
    ```bash
    (venv) $ flask run
    ```
