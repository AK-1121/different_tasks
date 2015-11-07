import re

def check_login(login):
    login = login.lower()
    pattern = re.compile("(^[a-z]$|^[a-z][a-z0-9.-]{0,18}[a-z0-9]$)")
    return bool(pattern.match(login))
