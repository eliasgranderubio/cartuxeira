import json
from flask import Blueprint
from utils.utils import is_valid_email
from analysis.email_risk_eval import get_email_risk_eval


# -- Global

risk_api = Blueprint('risk_api', __name__)


# -- APIs
@risk_api.route('/v1/risk/email/<string:email>', methods=['GET'])
def get_email_risk(email):
    if not is_valid_email(email):
        return json.dumps({'err': 400, 'msg': 'Bad email format'}, sort_keys=True), 400
    response = get_email_risk_eval(email)
    return json.dumps(response, sort_keys=True), 200
