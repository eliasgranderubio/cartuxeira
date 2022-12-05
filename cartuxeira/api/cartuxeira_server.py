import json
from flask import Flask
from waitress import serve
from api.blacklist.blacklist import bl_api
from api.riskEval.risk_eval import risk_api
from api.internal.internal_server import InternalServer


# Cartuxeira server class

class CartuxeiraServer:

    # -- Global attributes

    app = Flask(__name__)
    app.register_blueprint(bl_api)
    app.register_blueprint(risk_api)

    # -- Public methods

    # CartuxeiraServer Constructor
    def __init__(self, cartuxeira_server_host='127.0.0.1', cartuxeira_server_port=5000, mongodb_host='127.0.0.1',
                 mongodb_port=27017):
        super(CartuxeiraServer, self).__init__()
        self.cartuxeira_server_host = cartuxeira_server_host
        self.cartuxeira_server_port = cartuxeira_server_port
        InternalServer.set_mongodb_driver(mongodb_host, mongodb_port)

    # Runs CartuxeiraServer
    def run(self):
        serve(CartuxeiraServer.app, host=self.cartuxeira_server_host, port=self.cartuxeira_server_port, ident=None)

    # -- Post process

    # Apply headers
    @app.after_request
    def apply_headers(response):
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response

    # -- Error handlers

    # 400 Bad Request error handler
    @app.errorhandler(400)
    def bad_request(self):
        return json.dumps({'err': 400, 'msg': 'Bad Request'}, sort_keys=True), 400

    # 404 Not Found error handler
    @app.errorhandler(404)
    def not_found(self):
        return json.dumps({'err': 404, 'msg': 'Not Found'}, sort_keys=True), 404

    # 500 Internal Server error handler
    @app.errorhandler(500)
    def internal_server_error(self):
        return json.dumps({'err': 500, 'msg': 'Internal Server Error'}, sort_keys=True), 500
