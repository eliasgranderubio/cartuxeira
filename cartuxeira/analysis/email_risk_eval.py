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
