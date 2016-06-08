import os


def getIP(url, domainName):
    url = url[url.find(domainName):] 
    command = 'getent hosts ' + url
    process = os.popen(command)
    results = str(process.read())
    results = results.split()[0]
    return results
