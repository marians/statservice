# encoding: utf-8

from scipy.stats import spearmanr
from scipy.stats import linregress
import json
import datetime
import email.utils
import calendar

from flask import Flask
from flask import request
from flask import make_response
#from pprint import pprint

app = Flask(__name__)


@app.route('/')
def index():
    html = ''
    html += '<p>This is <b>statservice</b>, your friendly statistics webservice.</p>'
    html += '<p>Find out more about me at <a href="https://github.com/marians/statservice">my GitHub repository</a>.</p>'
    html += '<p>Functions on the menu are:</p>'
    html += '<ul>'
    html += '<li><a href="/api/linregress">/api/linregress</a></li>'
    html += '<li><a href="/api/spearmanr">/api/spearmanr</a></li>'
    html += '</ul>'
    html += '<p>Enjoy my CPU cycles and have a nice day!</p>'
    return html


@app.route('/api/linregress')
def stats_linregress():
    """
    Wrapper for scipy.stats.linregress
    """
    documentation = {
        'description': 'Calculate a linear regression from two lists',
        'url': 'http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html',
        'input': 'Two value lists of same length, given as comma-seperated floats or ints.',
        'output': [
            {
                'name': 'slope',
                'description': 'slope of the regression line'
            },
            {
                'name': 'intercept',
                'description': 'intercept of the regression line'
            },
            {
                'name': 'r',
                'description': 'Correlation coefficient'
            },
            {
                'name': 'rsquared',
                'description': 'r squared'
            },
            {
                'name': 'p',
                'description': 'two-sided p-value for a hypothesis test whose null hypothesis is that the slope is zero'
            },
            {
                'name': 'stderr',
                'description': 'Standard error of the estimate'
            }
        ],
        'examples': [
            '?a=1.1,2.1,3,4&b=4,2,8.0,9.4234'
        ]
    }
    a = None
    b = None
    try:
        a = [float(x) for x in request.args.get('a', '').split(',')]
        b = [float(x) for x in request.args.get('b', '').split(',')]
    except ValueError:
        return abort(400, 'Bad request parameters. Please read the docs, in case you find them.', documentation)
    if len(a) != len(b):
        return abort(400, 'Value list a and b MUST be of same length.', documentation)
    slope, intercept, r, p, stderr = linregress(a, b)
    output = json.dumps({
        'status': 200,
        'result': {
            'slope': slope,
            'intercept': intercept,
            'r': r,
            'rsquared': r ** 2,
            'p': p,
            'stderr': stderr
        }
    })
    callback = request.args.get('callback', '')
    if callback != '':
        output = '%s(%s)' % (callback, output)
    resp = make_response(output, 200)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Content-type'] = 'application/json'
    resp.headers['Expires'] = expires_date(hours=(24 * 30))
    return resp


@app.route('/api/spearmanr')
def stats_spearmanr():
    """
    Wrapper for scipy.stats.spearmanr
    """
    documentation = {
        'description': 'Calculate Spearman´s correlation coefficient rho from two lists',
        'url': 'http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.spearmanr.html',
        'input': 'Two value lists of same length, given as comma-seperated floats or ints.',
        'output': [
            {
                'name': 'rho',
                'description': 'Correlation coefficient, float between -1.0 and 1.0'
            },
            {
                'name': 'p',
                'description': 'The two-sided p-value for a hypothesis test whose null hypothesis is that two sets of data are uncorrelated'
            }
        ],
        'examples': [
            '?a=1.1,2.1,3,4&b=4,2,8.0,9.4234'
        ]
    }
    a = None
    b = None
    try:
        a = [float(x) for x in request.args.get('a', '').split(',')]
        b = [float(x) for x in request.args.get('b', '').split(',')]
    except ValueError:
        return abort(400, 'Bad request parameters. Please read the docs, in case you find them.', documentation)
    if len(a) != len(b):
        return abort(400, 'Value list a and b MUST be of same length.', documentation)
    (rho, p) = spearmanr(a, b)
    output = json.dumps({
        'status': 200,
        'result': {
            'rho': rho,
            'p': p
        }
    })
    callback = request.args.get('callback', '')
    if callback != '':
        output = '%s(%s)' % (callback, output)
    resp = make_response(output, 200)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Content-type'] = 'application/json'
    resp.headers['Expires'] = expires_date(hours=(24 * 30))
    return resp


def abort(code, msg, documentation):
    """Send error response"""
    output = json.dumps({
        'status': code,
        'message': msg,
        'documentation': documentation
    })
    resp = make_response(output, code)
    return resp


def rfc1123date(value):
    """Converts a date to a HTTP heade friendly (RFC 1123) format"""
    tpl = value.timetuple()
    stamp = calendar.timegm(tpl)
    return email.utils.formatdate(timeval=stamp, localtime=False, usegmt=True)


def expires_date(hours):
    """Date commonly used for Expires response header"""
    dt = datetime.datetime.now() + datetime.timedelta(hours=hours)
    return rfc1123date(dt)


if __name__ == '__main__':
    app.debug = True
    app.run()
