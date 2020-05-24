#!/usr/bin/env python
# coding: utf-8
# @Author: Sachin Pothukuchi
# @Date: 25/05/2020


import configparser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os
from bs4 import BeautifulSoup


class InternshalaBot():
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        
        #read config file for username and password and preset responses
        self.config = configparser.ConfigParser()
        self.config.read('internshalaConfig.ini')
     
    def login(self):
        
        #get the main internshala page
        self.driver.get('https://internshala.com/')
        
        #click on the main login button to begin login
        self.driver.find_element_by_xpath('//*[@id="register-button-positioner"]/button').click()
        
        #get login info
        email = self.config['login']['email']
        password = self.config['login']['password']
        
        #find login elements and input info
        email_field = self.driver.find_element_by_xpath('//*[@id="modal_email"]')
        email_field.send_keys(email)
        password_field = self.driver.find_element_by_xpath('//*[@id="modal_password"]')
        password_field.send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="modal_login_submit"]').click()
        
    def apply(self):
        '''Find the first internship available and apply
        The function loads into internshala filtered by preferences so your particular topic can come in
        It does not check for duration or stipend, those can be added easily by looking at the tags and I dont care about those
        '''
        
        sleep(5)
        
        #go to internship page that loads internships according to preferences
        self.driver.get('https://internshala.com/internships/matching-preferences')
        
        #find first internship and click on it
        self.driver.find_element_by_css_selector('#internship_list_container .view_detail_button').click()
        
        #click on apply now
        self.driver.find_element_by_xpath('//*[@id="search_button"]').click()
        
        #clicking on accepting the resume
        self.driver.find_element_by_xpath('//*[@id="application-button"]/button').click()
        
        #just works this way
        sleep(1)
        
        #filling the application
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        ids = [textarea['id'] for textarea in soup.find_all('textarea')]
        
        #go through all ids and fill in answers
        #I havent seen more than 4 questions in a form and they are as follows:
        # 1 -> Why are you fit for this
        # 2 -> Are you available
        # 3 -> Projects with links / Give your opinion on their website
        # 4 -> They can't pay for accomodation,etc can you handle it yourself
        for i,id_id in enumerate(ids):
            txt = self.driver.find_element_by_id(id_id)
            #clear any input put by internshala (it's buggy and doesnt do it all the time)
            txt.clear()
            txt.send_keys(self.config['Application']['answer'+str(i+1)])
        
        #click on submit
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        
        print('Applied')
        
    
    #rudimentary function in case you want to run the script all day long, wanna add scehduler etc properly
    def run(self, repeat=10, hours=1):
        '''repeat the number of times to apply to a new internship, scheduling'''
        while True:
            for i in range(repeat):
                try:
                    self.apply()
                except:
                    print('Could not apply')
            sleep(hours * 60 * 60)

if __name__ == '__main__':
    bot = InternshalaBot()
    bot.login()
    bot.run()

