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
