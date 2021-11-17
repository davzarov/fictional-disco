import math
import time
from calendar import timegm


def to_domain(domain: str) -> str:
    """formats domain as Netscape cookie format spec"""
    if not domain.startswith("."):
        # if domain starts with www
        if len(domain.split(".")) > 2:
            # prepend . and join anything after
            domain = "." + ".".join(domain.split(".")[-2:])
        else:
            # only prepend . and return
            domain = "." + domain
    else:
        # for cases like .www.domain.com
        domain = "." + ".".join(domain.split(".")[-2:])
    return domain


def iso_to_unix_time(expiration: str) -> int:
    """2021-08-27T13:42:19.439Z => Unix timestamp"""
    return timegm(time.strptime(expiration, '%Y-%m-%dT%H:%M:%S.%fZ'))


def session_to_unix_time() -> int:
    """Session => Unix timestamp"""
    return math.trunc(time.mktime(time.gmtime(time.time())))


def to_timestamp(expiration: str) -> str:
    if expiration in ["Session", "Sesión"]:
        return str(session_to_unix_time())
    return str(iso_to_unix_time(expiration))


def to_boolean(secure: str) -> str:
    return "TRUE" if secure == "✓" else "FALSE"


def to_dict(cookie_row: str) -> dict:
    keys = ["name", "value", "domain", "path", "expires", "size",
            "httpOnly", "secure", "sameSite", "sameParty", "Priority", "blank"]
    values = cookie_row.split("\t")
    return {k: v for k, v in zip(keys, values)}
