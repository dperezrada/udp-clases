import sqlite3
from flask import g, request

DATABASE = 'dummy.db'

import sqlite3
from flask import g

DATABASE = 'dummy.db'

from flask import Flask
app = Flask(__name__)
app.debug = True

def connect_db():
    return sqlite3.connect(DATABASE)

@app.before_request
def before_request():
    g.db = connect_db()

@app.after_request
def after_request(response):
    g.db.close()
    return response

def query_db(query, args=(), one=False):
    print "QUERY:", query
    print "ARGS:", args
    cur = g.db.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    return (rv[0] if rv else None) if one else rv


@app.route("/")
def bad_login():
    email = request.args.get('e')
    password = request.args.get('p')
    query = """SELECT *
    FROM accounts
    WHERE email = '%s' AND password = '%s';""" % (email, password)
    result = query_db(query)
    print query
    if len(result) > 0:
        return "Logeado"
    else:
        return "No logeado"
















@app.route("/safe")
def safe_login():
    email = request.args.get('e')
    password = request.args.get('p')
    query = "SELECT * from accounts where email = ? and password = ?;"
    params = [email, password]
    result = query_db(query, params)
    if len(result) > 0:
        return "Logeado"
    else:
        return "No logeado"

if __name__ == "__main__":
    app.run()
