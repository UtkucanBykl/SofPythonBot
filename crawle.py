#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2, sys
import bs4 as bs
from datetime import datetime
from database import Database

reload(sys)
sys.setdefaultencoding('utf-8')

db = Database()
page = 1
baseurl = "https://stackoverflow.com"
while(True):
    URL = "https://stackoverflow.com/questions/tagged/python?page="+str(page)+"&sort=votes&pagesize=50"
    sauce = urllib2.urlopen(URL).read()
    soup = bs.BeautifulSoup(sauce, "lxml")
    for div in soup.find_all('div', attrs={'class' : "question-summary"}):
        URLL = baseurl+div.find('a')["href"]
        saucee = urllib2.urlopen(URLL).read()
        soupp = bs.BeautifulSoup(saucee, "lxml")
        content =soupp.find("div", class_="post-text").text
        answer = soupp.find("td", class_="answercell").find("div", class_="post-text").text

        question = {
        "views" : div.find('div', class_="views").text,
        "status" : div.find('div', class_="status").text,
        "title" : div.find('a').text,
        "href" : URLL,
        "content" : content,
        "insertdate" : datetime.now().strftime("%d-%m-%y-%H-%M"),
        "answer":answer
        }

        db.Insert(question)
    page = page + 1