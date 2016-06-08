from general import *
from domainName import *
from ipAddress import *
from nmap import *
from robotsTxt import *
from whois import *


ROOT_DIR = 'companies'
createDir(ROOT_DIR)


def gatherInfo(name, url):
    domainName = getDomain(url)
    ipAddress = getIP(url, domainName)
    nmap = getNmap('-F', ipAddress)
    robotsTxt = getRobotsTxt(url)
    whois = getWhois(domainName)
    createReport(name, url, domainName, nmap, robotsTxt, whois)

def createReport(name, fullURL, domainName, nmap, robotsTxt, whois):
    projectDir = ROOT_DIR + '/' + name
    createDir(projectDir)
    writeFile(projectDir + '/fullURL.txt', fullURL)
    writeFile(projectDir + '/domainName.txt', domainName)
    writeFile(projectDir + '/nmap.txt', nmap)
    writeFile(projectDir + '/robotsTxt.txt', robotsTxt)
    writeFile(projectDir + '/whois.txt', whois)

name = input('Enter Name: ')
url = input('Enter URL: ')

gatherInfo(name, url)

while 1:
    exit = input('To continue press Y/y and to quit press N/n:  ')
    if exit.lower() == 'y':
        name = input('Enter Name: ')
        url = input('Enter URL: ')
        gatherInfo(name, url)
    elif exit.lower() == 'n':
        print('*************TADA***************')
        break
    else:
        print('Invalid option')
        break
