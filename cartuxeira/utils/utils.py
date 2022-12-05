import re


# -- Utils

# Check if email is valid
def is_valid_email(email):
    email_regex = re.compile(
        r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?")
    regex_validation = re.fullmatch(email_regex, email)
    return regex_validation is not None


# Check if domain is valid
def is_valid_domain(domain):
    domain_regex = re.compile(r"(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]")
    regex_validation = re.fullmatch(domain_regex, domain)
    return regex_validation is not None
