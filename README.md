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

## Installation

    virtualenv venv
    source venv/bin/activate
    pip install numpy
    pip install scipy
    pip install Flask

## Use

    cd webapp
    python app.py

## Kudos

* [SciPy](http://www.scipy.org/)
* [Flask](http://flask.pocoo.org/)
