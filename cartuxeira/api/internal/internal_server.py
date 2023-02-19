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
from driver.mongodb_driver import MongoDbDriver


# Internal server class

class InternalServer:

    # -- Global attributes

    _mongodb_driver = MongoDbDriver()
    _email_reputation_api_key = ''

    # Gets MongoDB Driver
    @staticmethod
    def get_mongodb_driver():
        return InternalServer._mongodb_driver

    # Gets Email Reputation API KEY
    @staticmethod
    def get_email_reputation_api_key():
        return InternalServer._email_reputation_api_key

    # Sets MongoDB Driver
    @staticmethod
    def set_mongodb_driver(mongodb_host, mongodb_port):
        if not mongodb_host:
            mongodb_host = '127.0.0.1'
        if not mongodb_port:
            mongodb_port = 27017
        InternalServer._mongodb_driver = MongoDbDriver(mongodb_host, mongodb_port)

    # Sets Email Reputation API KEY
    @staticmethod
    def set_email_reputation_api_key(api_key):
        InternalServer._email_reputation_api_key = api_key
