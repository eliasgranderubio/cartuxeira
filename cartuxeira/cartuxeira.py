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
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from cli.cliParser import CLIParser
from api.cartuxeira_server import CartuxeiraServer


# -- Main function
def main(parsed_args):
    server = CartuxeiraServer(cartuxeira_server_host=parsed_args.get_server_host(),
                              cartuxeira_server_port=parsed_args.get_server_port(),
                              mongodb_host=parsed_args.get_mongodb_host(),
                              mongodb_port=parsed_args.get_mongodb_port(),
                              email_reputation_api_key=parsed_args.get_email_reputation_api_key())
    server.run()


if __name__ == "__main__":
    main(CLIParser())
