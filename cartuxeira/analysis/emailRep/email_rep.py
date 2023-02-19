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
from emailrep import EmailRep
from api.internal.internal_server import InternalServer


# -----------------------------------------------------------
# Check email reputation
# -----------------------------------------------------------
def get_email_rep(email):
    # Init
    mongo_driver = InternalServer.get_mongodb_driver()
    info = {}

    # Local review
    if mongo_driver.is_email_rep_info(email):
        info = mongo_driver.get_email_rep_info(email)
    else:   # Online review
        # Setup your api key (optional)
        if not InternalServer.get_email_reputation_api_key():
            emailrep = EmailRep()
        else:
            emailrep = EmailRep(InternalServer.get_email_reputation_api_key())

        # Query an email address
        info = emailrep.query(email)
        mongo_driver.insert_email_rep_info(email, info)

    # Return
    del info["email"]
    return info
