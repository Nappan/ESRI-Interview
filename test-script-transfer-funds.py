import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

class TransferFunds(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_initialize_database(self):
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

        elem = driver.find_element_by_link_text("Open New Account")
        elem.click()
        time.sleep(1)

        elem = driver.find_element_by_xpath("//input[@class='button'][@type='submit'][@value='Open New Account']")
        elem.click()
        time.sleep(1)

        elem = driver.find_element_by_link_text("Transfer Funds")
        elem.click()
        time.sleep(1)

        elem = driver.find_element_by_xpath("//input[@id='amount'][@type='text']")
        elem.send_keys("50")

        select = Select(driver.find_element_by_xpath("//select[@id='toAccountId']"))
        select.select_by_value("13677")

        elem = driver.find_element_by_xpath("//input[@class='button'][@type='submit'][@value='Transfer']")
        elem.click()
        time.sleep(1)

        elem = driver.find_element_by_link_text("Find Transactions")
        elem.click()
        time.sleep(1)

        elem = driver.find_element_by_xpath("//input[@id='criteria.amount']")
        elem.send_keys("50")
        time.sleep(1)

        elem = driver.find_element_by_xpath("//button[@class='button' and contains(@ng-click, 'AMOUNT')]")
        elem.click()
        time.sleep(1)

        elem = driver.find_element_by_link_text("Funds Transfer Sent")
        elem.click()
        time.sleep(10)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()