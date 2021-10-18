def register_middleware(app):
    # Middleware para adicionar os headers do cors
    @app.after_request
    def set_cors(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
