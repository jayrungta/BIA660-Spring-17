# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 15:24:58 2017

@author: Harsh Kevadia, Jay Rungta, Manali Satghar, Anurag Patil, Abhijeet Parihar

A simple script that demonstrates how we classify textual data with sklearn.

"""
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
#read the reviews and their polarities from a given file
def loadData(fname):
    reviews=[]
    labels=[]
    f=open(fname)
    for line in f:
        review,rating=line.strip().split('\t')  
        reviews.append(review.lower())    
        labels.append(int(rating))
    f.close()
    return reviews,labels

rev_train,labels_train=loadData('reviews_train.txt')
rev_test,labels_test=loadData('reviews_test.txt')


#Build a counter based on the training dataset
counter = CountVectorizer()
counter.fit(rev_train)


#count the number of times each term appears in a document and transform each doc into a count vector
counts_train = counter.transform(rev_train)#transform the training data
counts_test = counter.transform(rev_test)#transform the testing data

#train classifier
clf = RandomForestClassifier(n_estimators=2855, criterion='entropy',max_features='log2', oob_score=True,max_depth=5000,min_samples_split=162,random_state=150, n_jobs=8)
#text_clf = Pipeline([('vect', CountVectorizer()),('tfidf', TfidfTransformer()),('clf', SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, n_iter=5, random_state=42)),])
#train all classifier on the same datasets
clf.fit(counts_train,labels_train)

#use hard voting to predict (majority voting)
pred=clf.predict(counts_test)

#print accuracy
print (accuracy_score(pred,labels_test))