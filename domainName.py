from tld import get_tld


def getDomain(url):
    domainName = get_tld(url)
    return domainName
