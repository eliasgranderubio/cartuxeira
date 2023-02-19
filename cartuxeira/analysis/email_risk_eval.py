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
from analysis.blacklist.blacklist import is_domain_blacklisted_offline
from analysis.blacklist.blacklist import is_domain_blacklisted_online
from analysis.dgaDetect.dga_detect import is_dga_domain
from analysis.blacklist.blacklist import is_email_blacklisted_offline
from analysis.emailRep.email_rep import get_email_rep


# Evaluates email risk relying on all included modules
def get_email_risk_eval(email):
    domain = email.split('@')[1]
    response = {}

    # -- Check domain
    d = {}
    d['is_in_offline_blacklist'] = is_domain_blacklisted_offline(domain)
    d['is_in_online_blacklist'] = is_domain_blacklisted_online(domain)
    d['is_dga'] = is_dga_domain(domain)

    # -- Check email
    e = {}
    e['is_in_offline_blacklist'] = is_email_blacklisted_offline(email)
    e['reputation'] = get_email_rep(email)

    # -- Return
    response['domain'] = d
    response['email'] = e
    return response
