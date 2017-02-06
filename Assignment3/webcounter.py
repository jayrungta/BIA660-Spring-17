#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 16:06:04 2017

@author: Jay

- Create a script called webcounter.py

- The script should define a function run() with 2 parameters: a link to webpage and a single word.

- The function should return the number of times that the word appears on the webpage

- Ignore case.

- Remove all non-letter characters before you count
"""


import re
from nltk.corpus import stopwords
import requests

def run(url, w): 

    freq=0 # counter of the frequency of the word 'w'

    stopLex=set(stopwords.words('english')) # build a set of english stopwrods 

    success=False# become True when we get the file

    for i in range(5): # try 5 times
        try:
            #use the browser to access the url 
            response=requests.get(url,headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })    
            success=True # success
            break # we got the file, break the loop
        except:# browser.open() threw an exception, the attempt to get the response failed
            print ('failed attempt',i)
     
    # all five attempts failed, return  None
    if not success: return None
    
    text=response.text # read in the text from the file
 
    sentences=text.split('.') # split the text into sentences 
	
    for sentence in sentences: # for each sentence 

        sentence=sentence.lower().strip() # lower case and strip	
        sentence=re.sub('[^a-z]',' ',sentence) # replace all non-letter characters  with a space
		
        words=sentence.split(' ') # split to get the words in the sentence 

        for word in words: # for each word in the sentence 
            if word=='' or word in stopLex: 
                continue # ignore empty words and stopwords 
            elif word == w: 
                freq = freq + 1 # update the frequency of the word 'w'
            
    #return the value of freq
    return freq

if __name__=='__main__':
    print(run('http://tedlappas.com/wp-content/uploads/2016/09/textfile.txt','amazon'))
	

	
