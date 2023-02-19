#
# Copyright 2023 The Cartuxeira Authors.
#
# Licensed to Dagda under one or more contributor
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
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
