from json import dumps
from bottle import route, run, response, request

@route('/to_download')
def list_to_download():
    urls = []
    response.content_type = 'application/json'
    return dumps(urls)

@route('/to_download', method=["POST"])
def add_to_download():
    print request.json
    response.content_type = 'application/json'
    return dumps([])

run(host='localhost', port=8080)
