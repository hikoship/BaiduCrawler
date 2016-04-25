# -*- coding: utf-8 -*-

import urllib, urllib.request
import sys
from bs4 import BeautifulSoup


word = input("Input your keywords: ") # keyword to be searched
maxNum = 200
num = input("Input the number of results you want (max = " + str(maxNum) + "): ") # num of news to be crawled
while True:
    try:
        num = min(int(num), 200)
        break
    except:
        print('Invalid value.')
        num = input("Input the number of results you want: ") # num of news to be crawled

rn = 50 # num of news per page

header = { 'Use-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6' }

page = 1

while num > 0:
    q = {}
    q['word'] = word
    if num > rn:
        q['rn'] = rn
    else:
        q['rn'] = num
    num = max(0, num - rn)
    q['pn'] = str(page - 1) + '0' # match Baidu page parameter
    q['tn'] = 'newstitle' # only shows title
    q=urllib.parse.urlencode(q)
    url = "http://news.baidu.com/ns?" + q

    # parse the page
    content = urllib.request.urlopen(url).read().decode('UTF-8')
    soup = BeautifulSoup(content, 'html.parser')

    for news in soup.select('.result'):

        link = news.h3.a
        tmpTitle = link.contents
        title = ''
        for e in tmpTitle:
            title += str(e)
        title = title.replace('<em>', '')
        title = title.replace('</em>', '')
        print (title)
        print (link['href'])

input("Press Enter to quit...")
