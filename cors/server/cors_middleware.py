class CorsMiddleware(object):
    """Simple Cors middleware"""
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        print "before request"
        def custom_start_response(status, headers, exc_info=None):
            headers.append(("Access-Control-Allow-Headers", "*"))
            headers.append(("Access-Control-Allow-Origin", "http://127.0.0.1:8000"))
            return start_response(status, headers, exc_info)
        response = self.app(environ, custom_start_response)
        print "post request"
        return response
