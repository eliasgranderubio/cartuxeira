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
