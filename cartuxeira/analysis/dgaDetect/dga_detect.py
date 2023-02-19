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
from dgad.prediction import Detective


# -----------------------------------------------------------
# Hunt domains generated by Domain Generation Algorithms
# -----------------------------------------------------------
def is_dga_domain(domain):
    temp_domains = [domain]
    detective = Detective()
    # convert temp_domains strings into dgad.schema.Domain
    temp_domains, _ = detective.prepare_domains(temp_domains)
    # classify them
    detective.investigate(temp_domains)
    # return if the domain is dga generated
    return temp_domains[0].is_dga
