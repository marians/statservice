statservice
===========

**A friendly web service for common statistical calculations, written in Python**

Think of it as a webservice wrapper for some SciPy functions.

This is in avery early phase and currently aims to provide the following functions:

### scipy.stats.linregress

Calculate the linear regression for value sets

Example:

    /api/linregress?a=1.1,2.1,3,4&b=4,2,8.0,9.4234&callback=jo

### scipy.stats.spearmanr

Calculate the Spearman correlation coefficient for two ranked value sets.

Example:

    /api/spearmanr?a=1.1,2.1,3,4&b=4,2,8.0,9.4234&callback=jo

## Requirements

Requires Python 2.6 or higher. Not tested with Python 3.*

## Installation / Quick start

1. Set up your python environment

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt


2. For development purposes, start the server like so:

    cd webapp
    python app.py

For actual production hosting, set up gunicorn and supervisor instead.

3. Setting up gunicorn

Copy the distributed config file to gunicorn.conf and change paths
according to your desires.

Test your configuriation like so:
	
	cd webapp
    gunicorn -c ../gunicorn.conf app:app

4. Set up supervisor

Copy the distributed config file to /etc/supervisor/conf.d/statserve.conf (or where ever your supervisor configs are) and change paths according to match your needs.


## Kudos

* [SciPy](http://www.scipy.org/)
* [Flask](http://flask.pocoo.org/)
