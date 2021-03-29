#This is a script to see if we are able to transfer $50 from one account to another, we will also be opening a new account for this customer

#DISCLAIMER: Account IDs are hard-coded in this script, which I understand is very bad practice, but for the sake of saving time and how this banking software works we will be hard coding the account IDs
#First Account ID is always 13566 while the second account ID is always 13677, if for whatever reason its assigned differently then it will need to be changed in the code.

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

class TransferFunds(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_initialize_database(self):
        #We will be starting in the index page
        driver = self.driver
        url="https://parabank.parasoft.com/parabank/index.htm"
        driver.get(url)
        self.assertIn("ParaBank", driver.title)

        #Same Login information for the user we created in previous scripts
        logusername = driver.find_element_by_xpath("//input[@class='input'][@name='username'][@type='text']")
        logpassword = driver.find_element_by_xpath("//input[@class='input'][@name='password'][@type='password']")
        logButton = driver.find_element_by_xpath("//input[@class='button'][@type='submit'][@value='Log In']")

        logusername.send_keys("Test")
        logpassword.send_keys("test123")
        logButton.click()
        time.sleep(1)

        #We will be clicking the link to create a new account
        elem = driver.find_element_by_link_text("Open New Account")
        elem.click()
        time.sleep(1)

        #We will be using default values for this one, just going to click the button to open up a new account.
        elem = driver.find_element_by_xpath("//input[@class='button'][@type='submit'][@value='Open New Account']")
        elem.click()
        time.sleep(1)

        #We will now be seeing if we can transfer some funds from our first account to our new account
        elem = driver.find_element_by_link_text("Transfer Funds")
        elem.click()
        time.sleep(1)

        #We will be transferring $50.00
        elem = driver.find_element_by_xpath("//input[@id='amount'][@type='text']")
        elem.send_keys("50")

        #The account ID for the "to Account # is hard coded here because for some reason it wouldn't let me select by index"
        select = Select(driver.find_element_by_xpath("//select[@id='toAccountId']"))
        #Second account ID goes here, if it's different, change it.
        select.select_by_value("13677")

        #Click button to complete transfer
        elem = driver.find_element_by_xpath("//input[@class='button'][@type='submit'][@value='Transfer']")
        elem.click()
        time.sleep(1)

        #We will now be verifying if the transaction went through
        elem = driver.find_element_by_link_text("Find Transactions")
        elem.click()
        time.sleep(1)

        #Since we sent $50.00, we will be finding transactions matching $50.00
        #WARNING: Due to the way the software is coded, this part can only properly work once, if the script needs to be ran twice, the database must be cleaned, and scripts must be ran from the beginning
        elem = driver.find_element_by_xpath("//input[@id='criteria.amount']")
        elem.send_keys("50")
        time.sleep(1)

        #Clicking the button right underneath the box that we just filled in
        elem = driver.find_element_by_xpath("//button[@class='button' and contains(@ng-click, 'AMOUNT')]")
        elem.click()
        time.sleep(1)

        #There should be an entry marked "Funds Transfer Sent", to verify if the transactions went through, we will click the entry. If everything passes, we should now be at a page with the transaction
        elem = driver.find_element_by_link_text("Funds Transfer Sent")
        elem.click()
        time.sleep(10)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()