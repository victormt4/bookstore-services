def register_middleware(app):
    @app.after_request
    def set_cors(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
