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

    def is_domain_in_local_black_list(self, domain):
        cursor = self.db.domain_local_bl.find({'_id': domain})
        return len(list(cursor)) > 0

    def is_email_in_local_black_list(self, email):
        cursor = self.db.email_local_bl.find({'_id': email})
        return len(list(cursor)) > 0

    def delete_domain_from_local_black_list(self, domain):
        self.db.domain_local_bl.delete_one({'_id': domain})

    def delete_email_from_local_black_list(self, email):
        self.db.email_local_bl.delete_one({'_id': email})
