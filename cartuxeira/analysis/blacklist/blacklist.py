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
