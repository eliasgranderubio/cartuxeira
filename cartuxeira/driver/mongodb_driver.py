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
import pymongo


class MongoDbDriver:

    # -- Public methods

    # MongoDbDriver Constructor
    def __init__(self, mongodb_host='127.0.0.1', mongodb_port=27017):
        super(MongoDbDriver, self).__init__()
        # Init
        self.client = pymongo.MongoClient(mongodb_host, mongodb_port)
        self.db = self.client.cartuxeira_database

    # -- CRUD methods

    def insert_domain_to_local_black_list(self, domain):
        self.db.domain_local_bl.insert_one({'_id': domain})

    def insert_email_to_local_black_list(self, email):
        self.db.email_local_bl.insert_one({'_id': email})

    def insert_email_rep_info(self, email, info):
        self.db.email_rep_info.insert_one({'_id': email, 'info': info})

    def is_domain_in_local_black_list(self, domain):
        return self.db.domain_local_bl.count_documents({'_id': domain}) > 0

    def is_email_in_local_black_list(self, email):
        return self.db.email_local_bl.count_documents({'_id': email}) > 0

    def is_email_rep_info(self, email):
        return self.db.email_rep_info.count_documents({'_id': email}) > 0

    def get_email_rep_info(self, email):
        if self.db.email_rep_info.count_documents({'_id': email}) == 0:
            return {}
        else:
            return self.db.email_rep_info.find_one({'_id': email})['info']

    def delete_domain_from_local_black_list(self, domain):
        self.db.domain_local_bl.delete_one({'_id': domain})

    def delete_email_from_local_black_list(self, email):
        self.db.email_local_bl.delete_one({'_id': email})

    def delete_email_rep_info(self, email):
        self.db.email_rep_info.delete_one({'_id': email})
