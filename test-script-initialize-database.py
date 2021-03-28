import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class CreateDatabase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_initialize_database(self):
        driver = self.driver
        url="https://parabank.parasoft.com/parabank/admin.htm"
        driver.get(url)
        self.assertIn("ParaBank", driver.title)

        elem = driver.find_element_by_xpath("//input[@id='accessMode2'][@class='input'][@name='accessMode'][@type='radio'][@value='restxml']")
        elem.click()

        elem = driver.find_element_by_xpath("//input[@class='button'][@type='submit'][@value='Submit']")
        elem.click()

        elem = driver.find_element_by_xpath("//button[@class='button'][@type='submit'][@name='action'][@value='CLEAN']")
        elem.click()

        elem = driver.find_element_by_xpath("//button[@class='button'][@type='submit'][@name='action'][@value='INIT']")
        elem.click()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()