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
        question = {
        "views" : div.find('div', class_="views").text,
        "status" : div.find('div', class_="status").text,
        "title" : div.find('a').text,
        "href" : baseurl+div.find('a')["href"],
        "content" : div.find('div', class_="excerpt").text,
        "insertdate" : datetime.now().strftime("%d-%m-%y-%H-%M")

        }
        db.Insert(question)
    page = page + 1