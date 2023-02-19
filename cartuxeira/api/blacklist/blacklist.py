#
# Copyright 2023 The Cartuxeira Authors.
#
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
import pymongo
from flask import Blueprint
from utils.utils import is_valid_email
from utils.utils import is_valid_domain
from api.internal.internal_server import InternalServer


# -- Global

bl_api = Blueprint('bl_api', __name__)


# -- CRUD APIs

@bl_api.route('/v1/bl/domain/<string:domain>', methods=['POST'])
def insert_domain_from_local_black_list(domain):
    if not is_valid_domain(domain):
        return json.dumps({'err': 400, 'msg': 'Bad domain format'}, sort_keys=True), 400
    try:
        InternalServer.get_mongodb_driver().insert_domain_to_local_black_list(domain)
        return json.dumps({}, sort_keys=True), 204
    except pymongo.errors.DuplicateKeyError:
        return json.dumps({'err': 409, 'msg': 'Domain already exists'}, sort_keys=True), 409


@bl_api.route('/v1/bl/domain/<string:domain>', methods=['GET'])
def is_domain_in_local_black_list(domain):
    if not is_valid_domain(domain):
        return json.dumps({'err': 400, 'msg': 'Bad domain format'}, sort_keys=True), 400
    included = InternalServer.get_mongodb_driver().is_domain_in_local_black_list(domain)
    if not included:
        return json.dumps({'err': 404, 'msg': 'Domain not found'}, sort_keys=True), 404
    return json.dumps({}, sort_keys=True), 204


@bl_api.route('/v1/bl/domain/<string:domain>', methods=['DELETE'])
def delete_domain_from_local_black_list(domain):
    if not is_valid_domain(domain):
        return json.dumps({'err': 400, 'msg': 'Bad domain format'}, sort_keys=True), 400
    InternalServer.get_mongodb_driver().delete_domain_from_local_black_list(domain)
    return json.dumps({}, sort_keys=True), 204


@bl_api.route('/v1/bl/email/<string:email>', methods=['POST'])
def insert_email_from_local_black_list(email):
    if not is_valid_email(email):
        return json.dumps({'err': 400, 'msg': 'Bad email format'}, sort_keys=True), 400
    try:
        InternalServer.get_mongodb_driver().insert_email_to_local_black_list(email)
        return json.dumps({}, sort_keys=True), 204
    except pymongo.errors.DuplicateKeyError:
        return json.dumps({'err': 409, 'msg': 'Email already exists'}, sort_keys=True), 409


@bl_api.route('/v1/bl/email/<string:email>', methods=['GET'])
def is_email_in_local_black_list(email):
    if not is_valid_email(email):
        return json.dumps({'err': 400, 'msg': 'Bad email format'}, sort_keys=True), 400
    included = InternalServer.get_mongodb_driver().is_email_in_local_black_list(email)
    if not included:
        return json.dumps({'err': 404, 'msg': 'Email not found'}, sort_keys=True), 404
    return json.dumps({}, sort_keys=True), 204


@bl_api.route('/v1/bl/email/<string:email>', methods=['DELETE'])
def delete_email_from_local_black_list(email):
    if not is_valid_email(email):
        return json.dumps({'err': 400, 'msg': 'Bad email format'}, sort_keys=True), 400
    InternalServer.get_mongodb_driver().delete_email_from_local_black_list(email)
    return json.dumps({}, sort_keys=True), 204
