import json
from flask import Blueprint
from utils.utils import is_valid_email
from api.internal.internal_server import InternalServer


# -- Global

bl_api = Blueprint('bl_api', __name__)


# -- APIs

@bl_api.route('/v1/bl/email/<string:email>', methods=['GET'])
def is_email_in_local_black_list(email):
    if not is_valid_email(email):
        return json.dumps({'err': 400, 'msg': 'Bad email format'}, sort_keys=True), 400
    included = InternalServer.get_mongodb_driver().is_email_in_local_black_list(email)
    if not included:
        return json.dumps({'err': 404, 'msg': 'Email not found'}, sort_keys=True), 404
    return json.dumps({}, sort_keys=True), 204
