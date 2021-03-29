# ESRI-Interview

We are going to be using ParaBank Banking Software to test our cases, I chose not to use an actual credit card/banking site because I didn't want to risk flagging systems for any sort of fraud while I test out my script.  

Test Cases:  
Verify if we can create a new database for a bank (test-script.initialize-database.py)  
Verify if we can register a new user into the bank (test-script-register.py)  
Verify if we can create a new account for our user (test-script-transfer-funds.py)  
Verify if we can transfer funds from one account to another (test-script-transfer-funds.py)  
Verify if we can request a loan from bank (test-script-request-loan.py)  

Requirements:  
Selenium  
Python 3.8  
FireFox  
geckodriver (https://github.com/mozilla/geckodriver/releases) - Place the geckodriver.exe file in the root of your Python directory  

How to run:
1. Run test-script.initialize-database.py
2. Run test-script-register.py
3. Run test-script-transfer-funds.py
4. Run test-script-request-loan.py

If any issues come up during the scripts, run the scripts from the beginning.  

#DISCLAIMER: Account IDs are hard-coded in this script, which I understand is very bad practice, but for the sake of saving time and how this banking software works I will be hard coding the account IDs