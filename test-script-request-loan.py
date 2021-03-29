#This is a script to verify if we are able to request a loan from the bank

#DISCLAIMER: Account IDs are hard-coded in this script, which I understand is very bad practice, but for the sake of saving time and how this banking software works we will be hard coding the account IDs
#Account ID is always 13566, if for whatever reason its assigned differently then it will need to be changed in the code.

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

class RequestLoan(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_register_user(self):
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

        #We will be clicking the button to Request a Loan
        elem = driver.find_element_by_link_text("Request Loan")
        elem.click()

        #We will be asking for a loan of $100.00
        elem = driver.find_element_by_xpath("//input[@id='amount' and contains(@ng-model, 'loanRequest.amount')]")
        elem.send_keys("100")

        #We will be making a Down Payment of $50.00 from our initial account
        elem = driver.find_element_by_xpath("//input[@id='downPayment' and contains(@ng-model, 'loanRequest.downPayment')]")
        elem.send_keys("50")

        #Account ID is hard coded here
        select = Select(driver.find_element_by_xpath("//select[@id='fromAccountId']"))
        #If the account ID is different, change it to the account ID that was created when the customer was registered
        select.select_by_value("13566")

        #We will be clicking the button now to process the loan
        elem = driver.find_element_by_xpath("//input[@class='button'][@type='submit'][@value='Apply Now']")
        elem.click()

        #We will now be verifying that the loan was processed
        elem = driver.find_element_by_link_text("Find Transactions")
        elem.click()
        time.sleep(1)

        #Account ID should be the same as the one we selected when creating the loan request
        select = Select(driver.find_element_by_xpath("//select[@id='accountId']"))
        #If the account ID is different, change it to the account ID that was created when the customer was registered
        select.select_by_value("13566")

        #Searching Transactions starting from the beginning of 2021
        elem = driver.find_element_by_xpath("//input[@id='criteria.fromDate']")
        elem.send_keys("01-01-2021")

        #Searching Transactions ending at the end of 2021
        elem = driver.find_element_by_xpath("//input[@id='criteria.toDate']")
        elem.send_keys("12-31-2021")

        #We will be searching by date range so click the "Find Transaction" under the Date Range section
        elem = driver.find_element_by_xpath("//button[@class='button' and contains(@ng-click, 'DATE_RANGE')]")
        elem.click()
        time.sleep(1)

        #If our loan was correctly processed, there should be an entry for "Down Payment for Loan", if it exists, script will attempt to click on it and test will pass, otherwise test will FAIL
        elem = driver.find_element_by_partial_link_text("Down Payment for Loan")
        elem.click()
        time.sleep(5)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()