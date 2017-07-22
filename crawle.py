#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2, sys
import bs4 as bs
from datetime import datetime
from database import Database

reload(sys)
sys.setdefaultencoding('utf-8')
post_text = []
db = Database()
page = 1
baseurl = "https://stackoverflow.com"
while(True):
    i = 0
    URL = "https://stackoverflow.com/questions/tagged/python?page="+str(page)+"&sort=votes&pagesize=50"
    sauce = urllib2.urlopen(URL).read()
    soup = bs.BeautifulSoup(sauce, "lxml")
    for div in soup.find_all('div', attrs={'class' : "question-summary"}):
        URLL = baseurl+div.find('a')["href"]
        saucee = urllib2.urlopen(URLL).read()
        soupp = bs.BeautifulSoup(saucee, "lxml")
        content =soupp.find("div", class_="post-text").text
        for div in soupp.find_all("div", class_="post-text"):
            if(i==2):
                break
            post_text.append(div.text)
            i = i + 1
        print(post_text[1])
        question = {
        "views" : div.find('div', class_="views").text,
        "status" : div.find('div', class_="status").text,
        "title" : div.find('a').text,
        "href" : URLL,
        "content" : post_text[0],
        "insertdate" : datetime.now().strftime("%d-%m-%y-%H-%M"),
        "answer":post_text[1]
        }

        db.Insert(question)
    page = page + 1