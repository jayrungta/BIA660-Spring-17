#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 15:33:05 2017

@author: Jay

4grams

Create script called parser.py. 

Your script should define the following functions:

 

processSentence(sentence,posLex,negLex,tagger):  The parameters of this function are a sentence (a string), a set positive words, a set of negative words, and a POS tagger.  The function should return a list with all the 4-grams in the sentence that have the following structure:                                                   

not <any word> <pos/neg word> <noun>. 

For example: not a good idea

 ---------------------------------------------------------------------------------------------

getTop3(D): The only parameter of this function is a dictionary D.  All the values in the dictionary are integers. The function returns a list of the keys with the 3 largest values in the dictionary.

 

Notes:

Don't change the names or the parameters of any of the functions
Make sure that your script imports all the libraries needed by the two functions

"""


import nltk
from nltk.util import ngrams
import re
from nltk.tokenize import sent_tokenize
from nltk import load
import collections

def processSentence(sentence,posLex,negLex,tagger):
     #tokenize the sentence
     terms = nltk.word_tokenize(sentence.lower())   

     POStags=['NN'] # POS tags of interest 		
     POSterms=getPOSterms(terms,POStags,tagger)
     nouns=POSterms['NN']

     result=[]

     fourgrams = ngrams(terms,4) #compute 2-grams
    
    #for each 2gram
     for fg in fourgrams:  
        if fg[0] == "not" and (fg[2] in posLex or fg[2] in negLex) and fg[3] in nouns: # if the 2gram is a an adverb followed by an adjective
             result.append(fg)
   
     return result

    
def getTop3(D):
    
    list = collections.Counter(D).most_common(3);
    result = [];
    for kv in list:
        result.append(kv[0]);
                      
    return result

def loadLexicon(fname):
    newLex=set()
    lex_conn=open(fname, mode='r', encoding='utf8')
    #add every word in the file to the set
    for line in lex_conn:
        newLex.add(line.strip())# remember to strip to remove the lin-change character
    lex_conn.close()

    return newLex   

# return all the terms that belong to a specific POS type
def getPOSterms(terms,POStags,tagger):
	
    tagged_terms=tagger.tag(terms)#do POS tagging on the tokenized sentence

    POSterms={}
    for tag in POStags:POSterms[tag]=set()

    #for each tagged term
    for pair in tagged_terms:
        for tag in POStags: # for each POS tag 
            if pair[1].startswith(tag): POSterms[tag].add(pair[0])

    return POSterms


def run(fpath):
    dict = {'abc':3,'jay':4, 'python':1, 'BIA':10, 'xyz':2}
    print(getTop3(dict));

    #load the positive and negative lexicon
    posLex=loadLexicon('positive-words.txt')
    negLex=loadLexicon('negative-words.txt')
    
    #make a new tagger
    _POS_TAGGER = 'taggers/maxent_treebank_pos_tagger/english.pickle'
    tagger = load(_POS_TAGGER)

    #read the input
    f=open(fpath)
    text=f.read().strip()
    f.close()

    #split sentences
    sentences=sent_tokenize(text)

    # for each sentence
    for sentence in sentences:

        sentence=re.sub('[^a-zA-Z\d]',' ',sentence)#replace chars that are not letters or numbers with a spac
        sentence=re.sub(' +',' ',sentence).strip()#remove duplicate spaces
        
        #get the results for this sentence 
        print(processSentence(sentence,posLex,negLex,tagger));
        
    return


if __name__=='__main__':
	run('input.txt')



