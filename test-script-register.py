#This is a test script to register a new user in our database, in this case the customer's name will be John Doe

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class RegisterUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_register_user(self):
        #Navigating to the registration page
        driver = self.driver
        url="https://parabank.parasoft.com/parabank/register.htm"
        driver.get(url)
        self.assertIn("ParaBank", driver.title)

        #Here we are assigning all the elements to variables
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

        #Using the variables we have created, we can now input all the information for our Test account in the database
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

        #After filling in all the boxes with information we will now click the Register button so that our account will be created
        elem = driver.find_element_by_xpath("//input[@class='button'][@type='submit'][@value='Register']")
        elem.click()
        time.sleep(1)

        #To test out if our account is working, we will first log out since it logs us in when registering
        elem = driver.find_element_by_link_text("Log Out")
        elem.click()
        time.sleep(1)

        #Assigning elements to variables
        logusername = driver.find_element_by_xpath("//input[@class='input'][@name='username'][@type='text']")
        logpassword = driver.find_element_by_xpath("//input[@class='input'][@name='password'][@type='password']")
        logButton = driver.find_element_by_xpath("//input[@class='button'][@type='submit'][@value='Log In']")

        #We will now be logging in using this information, this info will also be used in the remaining scripts
        logusername.send_keys("Test")
        logpassword.send_keys("test123")
        logButton.click()
        time.sleep(1)

        #We should now be logged in, just for verification purposes, we will have this script try to go to the update contact info page which should not be possible if we aren't logged in
        elem = driver.find_element_by_link_text("Update Contact Info")
        elem.click()
        time.sleep(5)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()