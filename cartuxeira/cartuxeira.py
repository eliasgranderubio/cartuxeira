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
