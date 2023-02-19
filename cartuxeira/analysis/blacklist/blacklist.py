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
import pydnsbl
from api.internal.internal_server import InternalServer


def is_domain_blacklisted_offline(domain):
    driver = InternalServer.get_mongodb_driver()
    return driver.is_domain_in_local_black_list(domain)


def is_email_blacklisted_offline(email):
    driver = InternalServer.get_mongodb_driver()
    return driver.is_email_in_local_black_list(email)


def is_domain_blacklisted_online(domain):
    domain_checker = pydnsbl.DNSBLDomainChecker()
    r = domain_checker.check(domain)
    return r.blacklisted
