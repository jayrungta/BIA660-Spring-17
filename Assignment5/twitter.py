#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 17:14:55 2017

@author: Jay

Extend the twitter.py script so that it also writes the following information for each tweet to the output file:

- The number of Favorites

- The number of Replies

- The date (Just day and month)
"""



from selenium import webdriver
import time

url='https://twitter.com/SHAQ'

#open the browser and visit the url
driver = webdriver.Chrome('./chromedriver')
driver.get(url)

#scroll down twice to load more tweets
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

#find all elements with a class that ends in 'tweet-text'
tweets=driver.find_elements_by_css_selector("[data-item-type=tweet]")

"""
for tweet in tweets:
    print (tweet.find_element_by_css_selector("[class$=tweet-text"))
"""

#write the tweets to a file
fw=open('tweets.txt','w', encoding='utf-8')
for tweet in tweets:
    txt,retweets,favorites,replies,date='NA','NA','NA','NA','NA'
    
    try: txt=tweet.find_element_by_css_selector("[class$=tweet-text]").text
    except: print ('no text')     

    try:
        #retweets
        retweetElement=tweet.find_element_by_css_selector("[class$=js-actionRetweet]")
        retweets=retweetElement.find_element_by_css_selector('[class=ProfileTweet-actionCountForPresentation]').text                                      
    
    except:
        print ('no retweets')

    try:
        #favorites
        favElement=tweet.find_element_by_css_selector("[class$=js-actionFavorite]")
        favorites=favElement.find_element_by_css_selector('[class=ProfileTweet-actionCountForPresentation]').text                                      
    
    except:
        print ('no favorites')

    try:
        #replies
        replyElement=tweet.find_element_by_css_selector("[class$=js-actionReply]")
        replies=replyElement.find_element_by_css_selector('[class=ProfileTweet-actionCountForPresentation]').text                                      
    
    except:
        print ('no replies')

    try:
        #date
        dateElement=tweet.find_element_by_css_selector("[class=time]")
        date=dateElement.find_element_by_css_selector("[data-long-form=true]").text                                      

    except:
        print ('no date')
        
    fw.write(txt.replace('\n',' ')+'\t'+str(retweets)+'\t'+str(favorites)+'\t'+str(replies)+'\t'+str(date)+'\n')


fw.close()


driver.quit()#close the browser
