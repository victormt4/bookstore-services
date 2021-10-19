def register_middleware(app):
    @app.after_request
    def set_cors(response):
        """
        Middleware para adicionar os headers do cors
        """
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
