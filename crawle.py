#!/usr/bin/env python
# -*- coding: utf-8 -*-
from imp import reload

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
        post_text = []
        URLL = baseurl+div.find('a')["href"]
        saucee = urllib2.urlopen(URLL).read()
        soupp = bs.BeautifulSoup(saucee, "lxml")
        content =soupp.find("div", class_="post-text").text
        answer1 = soupp.find("td", class_="answercell")
        answer =answer1.find("div" , class_ ="post-text").text
        print(answer)

        title = div.find("a").text

        question = {
        "title" : title,
        "href" : URLL,
        "content" : content,
        "insertdate" : datetime.now().strftime("%d-%m-%y-%H-%M"),
        "answer":answer
        }
        db.Insert(question)
        print(question)


        with open("deneme.txt", "a") as f:
            f.write(title+"\n")
    page = page + 1