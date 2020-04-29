from selenium import webdriver
from time import sleep

class starbot:
    def __init__(self,username,pw):
        self.driver = webdriver.Chrome(executable_path='F:\DOWNLOADS\chromedriver_win32\chromedriver.exe')
        self.username=username
        self.driver.get("https://.hotstar.com")
        sleep(2)
        self.driver.find_element_by_xpath("""//*[@id="app"]/div[2]/div/div[1]/div[1]/div/div[2]/div/div[5]/div""").click()
        sleep(2)
        self.driver.find_element_by_xpath("""//*[@id="app"]/div[2]/div/div[1]/div[3]/div/div/div[1]/div/div[2]/div/div[1]/div/div/button/div""")\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("""//*[@id="emailID"]""")\
            .send_keys(username)
        sleep(2)
        self.driver.find_element_by_xpath("""//*[@id="app"]/div[2]/div/div[1]/div[3]/div/div/div[1]/div/div[2]/div/div[1]/div/div/div[3]/button""")\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("""//*[@id="password"]""")\
            .send_keys(pw)
        sleep(2)
        self.driver.find_element_by_xpath("""//*[@id="app"]/div[2]/div/div[1]/div[3]/div/div/div[1]/div/div[2]/div/div[1]/div/div/div[3]/button""")\
            .click()
        sleep(20)
        
        
        
        
            
        
starbot("danadevashish@gmail.com","hotstar@1")