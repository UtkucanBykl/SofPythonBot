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
        post_text = []
        URLL = baseurl+div.find('a')["href"]
        saucee = urllib2.urlopen(URLL).read()
        soupp = bs.BeautifulSoup(saucee, "lxml")
        content =soupp.find("div", class_="post-text").text
        title = div.find("a").text
        for div in soupp.find_all("div", class_="post-text"):
            for k in range(2):
                post_text.append(div.text)

            question = {
        "title" : title,
        "href" : URLL,
        "content" : post_text[0],
        "insertdate" : datetime.now().strftime("%d-%m-%y-%H-%M"),
        "answer":post_text[1]
        }
            db.Insert(question)
            print(question)
            post_text.remove(post_text[0])
            post_text.remove(post_text[0])

        with open("deneme.txt", "a") as f:
            f.write(title+"\n")
    page = page + 1