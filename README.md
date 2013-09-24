statservice
===========

**A friendly web service for common statistical calculations, written in Python**

Think of it as a webservice wrapper for some SciPy functions.

This is in avery early phase and currently aims to provide only one function:

## Spearman's correlation

The correlation coefficient for two ranked value sets.

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