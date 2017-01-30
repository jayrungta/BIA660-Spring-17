#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 15:56:17 2017

@author: Jay

Write a script called senticounter.py. Define a function run() inside senticounter.py.

The function should:

- Accept as a parameter the path to a text file. The text file has one review per line. 

- Read the list of positive words from the positive-words.txt file.

- Create a dictionary that includes one key for each positive word that appears in the input text file. The dictionary should map each of these positive words to the number of reviews that include it. For example, if the word "great" appears in 5 reviews, then the dictionary should map the key "great" to the value 5. 

- Return the dictionary 

Notes: Ignore case. You can also assume that the input file includes only letters, no punctuation or other special characters.
"""

#function that loads a lexicon of positive words to a set and returns the set
def loadLexicon(fname):
    newLex=set()
    lex_conn=open(fname, mode='r', encoding='utf8')
    #add every word in the file to the set
    for line in lex_conn:
        newLex.add(line.strip())# remember to strip to remove the lin-change character
    lex_conn.close()

    return newLex

def run(path):
    #creating an empty dictionary
    dict = {}
    #load the positive lexicon
    posLex=loadLexicon('positive-words.txt')
    
    fin=open(path) # open the file
    for line in fin: # for every line in the file (1 review per line)
        posList=[] # list of positive words in the review
        
        line=line.lower().strip()   # cleaning the input line
        
        words=line.split(' ') # split on the space to get list of words
   
        for word in words: #for every word in the review
            if word in posLex: # if the word is in the positive lexicon
                if word not in posList: # if the word is not already present in the posList
                    posList.append(word) # add this word to the posList for this review
            
        for word in posList: # for every word in the posList
            if word in dict: 
                dict[word] = dict[word] + 1  # if the word is already in the dictionary increase its count by 1
            else:
                dict[word] = 1 # if it is not in dictionary set its count to 1
            
    fin.close() # close the file
    return dict # returning the dictionary

#main
if __name__ == "__main__": 
    print(run('textfile'))  # running the function

        