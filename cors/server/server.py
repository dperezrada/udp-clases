# -*- coding: utf-8 -*-
import json
from time import sleep

from flask import Flask, Response

from cors_middleware import CorsMiddleware
from cache_middleware import CacheMiddleware

DEFAULT_DELAY=1.5

# create our little application :)
app = Flask(__name__)

def return_json(data, status=200):
    return Response(response=json.dumps(data),
        status=status, \
        mimetype="application/json")

@app.route('/v1/cursos')
def list_cursos():
    print "listar cursos"
    sleep(DEFAULT_DELAY)
    to_return = [
        {
            'id': i,
            'name': 'Example %s' % i
        }
        for i in range(1, 10)
    ]
    return return_json(to_return)


@app.route('/v1/cursos/<curso_id>')
def get_curso(curso_id):
    print "get curso %s" % curso_id
    sleep(DEFAULT_DELAY)
    to_return = {
        'id': curso_id,
        'name': 'Example %s' % curso_id
    }
    return return_json(to_return)

app.wsgi_app = CacheMiddleware(CorsMiddleware(app.wsgi_app))

if __name__ == "__main__":
    app.run(debug=True)
