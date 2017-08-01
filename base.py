import pandas
import numpy    as np
from pandas import DataFrame
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

class MachineLearning():

    def __init__(self):
        questions = []
        with open("deneme.txt", "r") as f:
            for line in f:
                questions.append(line)

        status = []
        for i in range(len(questions)):
            status.append(i)
        self.__data = {'text': questions, 'status': status}


    def frame(self):
        frame = pandas.DataFrame(self.__data)
        self.frame_x=frame["text"]
        self.frame_y=frame["status"]



    def learning(self):
        self.vect = TfidfVectorizer(min_df=1)
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.frame_x, self.frame_y, test_size=0.2, random_state=4)
        self.x_trainvect = self.vect.fit_transform(self.x_train)
        self.x_trainvect.toarray()
        self.vect1 = TfidfVectorizer(min_df=1)
        self.x_trainvect = self.vect1.fit_transform(self.x_train)
        a = self.x_trainvect.toarray()
        self.vect1.inverse_transform(a[0])


    def bayes(self):
        self.mnb = MultinomialNB()
        self.y_train=self.y_train.astype('int')
        self.mnb.fit(self.x_trainvect,self.y_train)


    def find(self, sentence):
        self.frame()
        self.learning()
        self.bayes()
        x_testvect = self.vect1.transform([sentence])
        pred = self.mnb.predict(x_testvect)
        return self.frame_x[pred[0]]
