from driver.mongodb_driver import MongoDbDriver


# Internal server class

class InternalServer:

    # -- Global attributes

    _mongodb_driver = MongoDbDriver()

    # Gets MongoDB Driver
    @staticmethod
    def get_mongodb_driver():
        return InternalServer._mongodb_driver

    # Sets MongoDB Driver
    @staticmethod
    def set_mongodb_driver(mongodb_host, mongodb_port):
        if not mongodb_host:
            mongodb_host = '127.0.0.1'
        if not mongodb_port:
            mongodb_port = 27017
        InternalServer._mongodb_driver = MongoDbDriver(mongodb_host, mongodb_port)
