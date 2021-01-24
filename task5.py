# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 17:03:01 2021

@author: Preshita
"""

from selenium import webdriver
import time
import pandas as pd
import sqlite3 as sql

url = "https://www.etsy.com/in-en/listing/771086187/layered-heart-anklet-personalized-gold?ga_order=most_relevant&ga_search_type=all"
driver = webdriver.Chrome()
driver.get(url)
review_list = []

org = driver.find_element_by_css_selector('#reviews > div.wt-flex-xl-5.wt-flex-wrap > nav > ul > li:nth-child(5) > a')                                         
val = org.get_attribute("data-page")

j=2
while j<=int(val)+1:
    time.sleep(3)
    for i in range(3):
        review1 = driver.find_elements_by_css_selector("#review-preview-toggle-"+str(i))    
        for r in review1:
            review_list.append(r.text)
    if driver.find_elements_by_css_selector("#review-preview-toggle-3"):
        review1 = driver.find_elements_by_css_selector("#review-preview-toggle-3")  
        for r in review1:
            review_list.append(r.text)
    else:
        pass
    time.sleep(3)    
    if j<=3 or j==int(val):
        nextpage = driver.find_element_by_css_selector('#reviews > div.wt-flex-xl-5.wt-flex-wrap > nav > ul > li:nth-child(6) > a').click()
    elif (j>3 and j<int(val)):
        nextpage = driver.find_element_by_css_selector('#reviews > div.wt-flex-xl-5.wt-flex-wrap > nav > ul > li:nth-child(7) > a').click()                                              
    j=j+1

driver.close()

for i in review_list:
    print(i)
print(len(review_list))
df = pd.DataFrame(review_list,columns=["Reviews"]) 
#print(df) 
df.to_csv('reviews.csv')


conn = sql.connect('etsy_review.db')
df.to_sql('etsy1',conn)
new_df = pd.read_sql('SELECT * FROM etsy1',conn)
#print(new_df)