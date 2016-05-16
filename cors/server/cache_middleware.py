import os
import pickle

TARGET_FILE = '/tmp/cache_udp.txt'

class CacheMiddleware(object):
    """Simple Cors middleware"""
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        if environ.get('QUERY_STRING', '').find('reset_cache=') >= 0:
            print "resetting cache"
            os.remove(TARGET_FILE)
        if os.path.exists(TARGET_FILE):
            print "using cache"
            response = pickle.loads(open(TARGET_FILE).read())
            start_response('200 OK', [('Content-type', 'application/json'),])
            return response

        response = list(self.app(environ, start_response))

        with open(TARGET_FILE, "wb") as file_:
            print "writing cache"
            file_.write(pickle.dumps(response))
        return response
