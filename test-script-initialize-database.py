#This is a script to create the database that we will be using for our other test scripts

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class CreateDatabase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_initialize_database(self):
        #Logging into the admin portal of ParaBank to initialize all the back end stuff
        driver = self.driver
        url="https://parabank.parasoft.com/parabank/admin.htm"
        driver.get(url)
        self.assertIn("ParaBank", driver.title)

        #Making sure that Data Access Mode is set to REST (XML)
        elem = driver.find_element_by_xpath("//input[@id='accessMode2'][@class='input'][@name='accessMode'][@type='radio'][@value='restxml']")
        elem.click()

        #Clicking Submit to save changes
        elem = driver.find_element_by_xpath("//input[@class='button'][@type='submit'][@value='Submit']")
        elem.click()

        #Cleaning database first in case there was already data inside
        elem = driver.find_element_by_xpath("//button[@class='button'][@type='submit'][@name='action'][@value='CLEAN']")
        elem.click()

        #Initializing database for use with our other test scripts
        elem = driver.find_element_by_xpath("//button[@class='button'][@type='submit'][@name='action'][@value='INIT']")
        elem.click()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()