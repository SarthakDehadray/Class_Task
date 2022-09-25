# youtube scraping using selenium

from flask import Flask,request,jsonify
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sys
import time
import csv
import io
import pandas as pd
import os

app = Flask(__name__)

@app.route("/add",methods = ['GET'])
def scrape():
    l = ['https://www.youtube.com/user/krishnaik06/videos']
   
    for i in l:
        number = 0
        driver = webdriver.Chrome()
        driver.get(i)
        driver.maximize_window()
        time.sleep(10)
        all_links = driver.find_elements(By.TAG_NAME,"a")
        l = []
        for link in all_links:
            link_list = link.get_attribute("href")
            link_list = str(link_list)
            if len(link_list) == 43 and link_list not in l:
                l.append(link_list)
        driver.close()    
        for j in l[0:3]:
                    vid_number = 0
                    driver = webdriver.Chrome()             
                    driver.get(j)
                    driver.maximize_window()
                    time.sleep(10)
                 
                    try:
                        title = driver.find_element("xpath",'//*[@id="container"]/h1/yt-formatted-string').text
                        comment_section = driver.find_element("xpath",'//*[@id="comments"]')
                        views = driver.find_element("xpath",'//*[@id = "count"]/ytd-video-view-count-renderer/span[1]').text
                        date = driver.find_element("xpath",'//*[@id="info-strings"]/yt-formatted-string').text
                        channel = driver.find_element("xpath",'//*[@id="text"]/a').text
                        subscribers = driver.find_element("xpath",'//*[@id="owner-sub-count"]').text
                        description = driver.find_element("xpath",'//*[@id="description"]/yt-formatted-string').text
                        
                    except exceptions.NoSuchElementException:
                        error = "Error: Double check selector OR "
                        error += "element may not yet be on the screen at the time of the find operation"
                        print(error)

                    driver.execute_script("arguments[0].scrollIntoView();", comment_section)
                    time.sleep(5)

                    last_height = driver.execute_script("return document.documentElement.scrollHeight")

                    while True:
                        
                        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
                        time.sleep(2)
                        new_height = driver.execute_script("return document.documentElement.scrollHeight")
                        if new_height == last_height:
                            break
                        last_height = new_height

                    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")

                    try:
                        # Extract the elements storing the usernames and comments.
                        username_elems = driver.find_elements("xpath",'//*[@id="author-text"]')
                        comment_elems = driver.find_elements("xpath",'//*[@id="content-text"]')
                        
                    except exceptions.NoSuchElementException:
                        error = "Error: Double check selector OR "
                        error += "element may not yet be on the screen at the time of the find operation"
                        print(error)
                        
                    with io.open('basicinfo{}_{}.csv'.format(number,vid_number),'w',newline='',encoding="utf-16") as file:
                        writer = csv.writer(file,delimiter=",",quoting=csv.QUOTE_ALL)
                        writer.writerow(["Title","Views","Date","Channelname","subs","des","link"])
                        writer.writerow([title,views,date,channel,subscribers,description,j])
                        

                    # to read csv file named "samplee"
                    a = pd.read_csv("basicinfo{}_{}.csv".format(number,vid_number),encoding="utf-16")

                    # to save as html file
                    # named as "Table"
                    a.to_html("basicinfo{}_{}.htm".format(number,vid_number))

                    with io.open('comments{}_{}.csv'.format(number,vid_number), 'w', newline='', encoding="utf-16") as file:
                        writer = csv.writer(file, delimiter =",", quoting=csv.QUOTE_ALL)
                        writer.writerow(["Username", "Comment"])
                        for username, comment in zip(username_elems, comment_elems):
                            writer.writerow([username.text, comment.text])
                            
                    # to read csv file named "samplee"
                    a = pd.read_csv("comments{}_{}.csv".format(number,vid_number),encoding="utf-16")

                    # to save as html file
                    # named as "Table"
                    a.to_html("comments{}_{}.htm".format(number,vid_number))
                    vid_number = vid_number + 1
                    driver.close()
                    number = number + 1

if __name__ == "__main__":
   app.run(port = 5001)

