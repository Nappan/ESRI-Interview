import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

class RegisterUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_register_user(self):
        driver = self.driver
        url="https://parabank.parasoft.com/parabank/index.htm"
        driver.get(url)
        self.assertIn("ParaBank", driver.title)

        logusername = driver.find_element_by_xpath("//input[@class='input'][@name='username'][@type='text']")
        logpassword = driver.find_element_by_xpath("//input[@class='input'][@name='password'][@type='password']")
        logButton = driver.find_element_by_xpath("//input[@class='button'][@type='submit'][@value='Log In']")

        logusername.send_keys("Test")
        logpassword.send_keys("test123")
        logButton.click()
        time.sleep(1)

        elem = driver.find_element_by_link_text("Request Loan")
        elem.click()

        elem = driver.find_element_by_xpath("//input[@id='amount' and contains(@ng-model, 'loanRequest.amount')]")
        elem.send_keys("100")

        elem = driver.find_element_by_xpath("//input[@id='downPayment' and contains(@ng-model, 'loanRequest.downPayment')]")
        elem.send_keys("50")

        select = Select(driver.find_element_by_xpath("//select[@id='fromAccountId']"))
        select.select_by_value("13566")

        elem = driver.find_element_by_xpath("//input[@class='button'][@type='submit'][@value='Apply Now']")
        elem.click()

        elem = driver.find_element_by_link_text("Find Transactions")
        elem.click()
        time.sleep(1)

        select = Select(driver.find_element_by_xpath("//select[@id='accountId']"))
        select.select_by_value("13566")

        elem = driver.find_element_by_xpath("//input[@id='criteria.fromDate']")
        elem.send_keys("01-01-2021")

        elem = driver.find_element_by_xpath("//input[@id='criteria.toDate']")
        elem.send_keys("12-31-2021")

        elem = driver.find_element_by_xpath("//button[@class='button' and contains(@ng-click, 'DATE_RANGE')]")
        elem.click()
        time.sleep(1)

        elem = driver.find_element_by_partial_link_text("Down Payment for Loan")
        elem.click()
        time.sleep(5)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()