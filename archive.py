#!/usr/bin/python3

from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

def main():
    url = input('Enter Your Target: ')
    target = url
    print('Scanning the target', target)
    myurl = 'https://web.archive.org/cdx/search/cdx?url=*.'+target+'/*&output=text&fl=original&collapse=urlkey'

    uClient = req(myurl)
    page_html = uClient.read()
    uClient.close()

    parser = soup(page_html, "html.parser")
    print(parser)

    outfile = open('archive-out.txt', 'w')
    outfile.write(str(parser))
    outfile.close

main()
