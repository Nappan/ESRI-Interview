import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class RegisterUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_register_user(self):
        driver = self.driver
        url="https://parabank.parasoft.com/parabank/register.htm"
        driver.get(url)
        self.assertIn("ParaBank", driver.title)

        firstName = driver.find_element_by_xpath("//input[@id='customer.firstName'][@class='input'][@name='customer.firstName'][@type='text']")
        lastName = driver.find_element_by_xpath("//input[@id='customer.lastName'][@class='input'][@name='customer.lastName'][@type='text']")
        streetAddress = driver.find_element_by_xpath("//input[@id='customer.address.street'][@class='input'][@name='customer.address.street'][@type='text']")
        cityAddress = driver.find_element_by_xpath("//input[@id='customer.address.city'][@class='input'][@name='customer.address.city'][@type='text']")
        stateAddress = driver.find_element_by_xpath("//input[@id='customer.address.state'][@class='input'][@name='customer.address.state'][@type='text']")
        zipCodeAddress = driver.find_element_by_xpath("//input[@id='customer.address.zipCode'][@class='input'][@name='customer.address.zipCode'][@type='text']")
        phoneNumber = driver.find_element_by_xpath("//input[@id='customer.phoneNumber'][@class='input'][@name='customer.phoneNumber'][@type='text']")
        ssn = driver.find_element_by_xpath("//input[@id='customer.ssn'][@class='input'][@name='customer.ssn'][@type='text']")
        username = driver.find_element_by_xpath("//input[@id='customer.username'][@class='input'][@name='customer.username'][@type='text']")
        password = driver.find_element_by_xpath("//input[@id='customer.password'][@class='input'][@name='customer.password'][@type='password']")
        confirmPassword = driver.find_element_by_xpath("//input[@id='repeatedPassword'][@class='input'][@name='repeatedPassword'][@type='password']")

        firstName.send_keys("John")
        lastName.send_keys("Doe")
        streetAddress.send_keys("123 Fake Street")
        cityAddress.send_keys("Fake City")
        stateAddress.send_keys("California")
        zipCodeAddress.send_keys("12345")
        phoneNumber.send_keys("(555)555-5555")
        ssn.send_keys("123-45-6789")
        username.send_keys("Test")
        password.send_keys("test123")
        confirmPassword.send_keys("test123")

        elem = driver.find_element_by_xpath("//input[@class='button'][@type='submit'][@value='Register']")
        elem.click()

        elem = driver.find_element_by_link_text("Log Out")
        elem.click()

        logusername = driver.find_element_by_xpath("//input[@class='input'][@name='username'][@type='text']")
        logpassword = driver.find_element_by_xpath("//input[@class='input'][@name='password'][@type='password']")
        logButton = driver.find_element_by_xpath("//input[@class='button'][@type='submit'][@value='Log In']")

        logusername.send_keys("Test")
        logpassword.send_keys("test123")
        logButton.click()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()