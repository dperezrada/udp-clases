import sqlite3
from flask import g, request

DATABASE = 'dummy.db'

from flask import Flask
app = Flask(__name__)
app.debug = True


@app.route("/")
def home():
    image_number = request.args.get('i')
    image_url = "http://www.laramontours.com/gallery/images/album1/%s.jpg" % image_number
    return """<!DOCTYPE html>
<html>
<head>
    <title></title>
    <script src="https://code.jquery.com/jquery-1.12.3.min.js"></script>
</head>
<body>
    <img src='%s'/>
</body>
</html>""" % image_url

if __name__ == "__main__":
    app.run()
