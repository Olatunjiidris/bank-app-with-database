import sys
import time
import random
import mysql.connector as sql
mycon = sql.connect(host = "localhost", user = "root", password = "", database = "atm_db")
class atm:
    def __init__(self):
        self.name = ""
        self.password = ""
        self.homePage()
    def homePage(self):
        print("""
                Welcome to Coded Bank

            1. Sign in
            2. Sign up
            3. Quit
        """)
        self.user = input(">>> ")
        if self.user == "1":
            self.signIn()
        elif self.user == "2":
            self.signUp()
        elif self.user == "3":
            sys.exit()
        else:
            self.homePage()
        
    def signIn(self):
        print("""
                put your username and password here
        """)
        self.name = input("Username: ")
        self.password = input("Password: ")
        self.mycursor = mycon.cursor()
        self.query = ("SELECT USER_NAME, PASS_WORD FROM customers_info WHERE USER_NAME = %s and PASS_WORD =%s")
        self.val = (self.name,self.password)
        self.mycursor.execute(self.query, self.val)
        self.myreg = self.mycursor.fetchone()
        if self.myreg:
            self.operation()
        else:
            print("Wrong credential")
            self.signIn()
        
    def operation(self):
        print("""
                1. Deposit                2. Withdrawal
                3. Transfer               4. Airtime
                5. Check Balance          6. Log out
                7. Exit 
        """)
        self.user = input(">>> ")
        if self.user == "1":
            self.deposit()
        elif self.user == "2":
            self.withdrawal()
        elif self.user == "3":
            self.transfer()
        elif self.user == "4":
            self.airtime()
        elif self.user == "5":
            self.check()
        elif self.user == "6":
            self.homePage()
        elif self.user == "7":
            sys.exit()
        else:
            print("invalid input!")
            self.operation()

    def deposit(self):
        self.user1 = int(input("How much will you like to deposit: $"))
        time.sleep(1)
        print("The deposit of $" + str(self.user1) + " was successful\npress 0 to go back")
        self.query = "SELECT BALANCE FROM customers_info WHERE USER_NAME = %s and PASS_WORD =%s"
        self.val = (self.name,self.password)
        self.mycursor.execute(self.query, self.val)
        self.x = self.mycursor.fetchone()
        self.b = list(self.x)
        for i in self.b:
            self.balance = int(i)
        self.balance1 = self.balance + self.user1
        self.query = "UPDATE customers_info SET BALANCE='%s' WHERE USER_NAME = %s and PASS_WORD =%s"
        self.val = (self.balance1,self.name,self.password)
        self.mycursor.execute(self.query, self.val)
        mycon.commit()
        self.user2 = input("")
        if self.user2 == "0":
            self.operation()
        else:
            print("invalid input!")
            self.deposit()

    def withdrawal(self):
        self.user1 = int(input("How much will you like to withdraw: $"))
        self.query = "SELECT BALANCE FROM customers_info WHERE USER_NAME = %s and PASS_WORD =%s"
        self.val = (self.name,self.password)
        self.mycursor.execute(self.query, self.val)
        self.x = self.mycursor.fetchone()
        self.b = list(self.x)
        for i in self.b:
            self.balance = int(i)
        if self.balance >= self.user1:
            time.sleep(1)
            print("The withdrawal of $" + str(self.user1) + " was successful, take your cash.\npress 0 to go back")
            self.balance1 = self.balance - self.user1
            self.query = "UPDATE customers_info SET BALANCE='%s' WHERE USER_NAME = %s and PASS_WORD =%s"
            self.val = (self.balance1,self.name,self.password)
            self.mycursor.execute(self.query, self.val)
            mycon.commit()
 
            self.user2 = input("")
            if self.user2 == "0":
                self.operation()
            else:
                print("invalid input!")
                self.withdrawal()
        else:
            print("you do not have sufficient balance")
            self.withdrawal()
    
    def transfer(self):
        self.user1 = int(input("How much will you like to transfer: $"))
        self.query = "SELECT BALANCE FROM customers_info WHERE USER_NAME = %s and PASS_WORD =%s"
        self.val = (self.name,self.password)
        self.mycursor.execute(self.query, self.val)
        self.x = self.mycursor.fetchone()
        self.b = list(self.x)
        for i in self.b:
            self.balance = int(i)
        if self.balance >= self.user1:
            print("These are the accounts you can transfer to ... ")
            time.sleep(1)
            self.query2 = "SELECT * FROM customers_info"
            self.mycursor.execute(self.query2)
            self.output = self.mycursor.fetchall()
            for a in self.output:
                print(a)
            self.enter = input("account number: ")
            self.query3 = "SELECT BALANCE FROM customers_info WHERE ACCT_NO =%s"
            self.val2 = (self.enter,)
            self.mycursor.execute(self.query3, self.val2)
            self.pick = self.mycursor.fetchall()
            if self.pick:
                self.a = self.pick[0][0]
                self.balance3 = int(self.a)
                self.balance4 = self.balance3 + self.user1
                self.query4 = "UPDATE customers_info SET BALANCE='%s' WHERE ACCT_NO= %s"
                self.val3 = (self.balance4,self.enter)
                self.mycursor.execute(self.query4, self.val3)
                mycon.commit()
                time.sleep(1)
                print("Transfer successful\npress 0 to go back")
            else:
                print("Account number no found")
            self.balance1 = self.balance - self.user1
            self.query = "UPDATE customers_info SET BALANCE='%s' WHERE USER_NAME = %s and PASS_WORD =%s"
            self.val = (self.balance1,self.name,self.password)
            self.mycursor.execute(self.query, self.val)
            mycon.commit()
 
            self.user2 = input("")
            if self.user2 == "0":
                self.operation()
            else:
                print("invalid input!")
                self.transfer()
        else:
            print("you do not have sufficient balance\npress 0 to go back")
            self.transfer()

    def airtime(self):
        self.user1 = int(input("How much airtime will you like to buy: $"))
        self.query = "SELECT BALANCE FROM customers_info WHERE USER_NAME = %s and PASS_WORD =%s"
        self.val = (self.name,self.password)
        self.mycursor.execute(self.query, self.val)
        self.x = self.mycursor.fetchone()
        self.b = list(self.x)
        for i in self.b:
            self.balance = int(i)
        if self.balance >= self.user1:
            self.input = input("phone number: ")
            time.sleep(1)
            print("The airtime of $" + str(self.user1) + " to " + str(self.input) + " was successful\npress 0 to go back")
            self.user2 = input("")
            if self.user2 == "0":
                self.operation()
            else:
                print("invalid input!")
                self.airtime()
        else:
            print("you do not have sufficient balance")
            self.airtime()
    
    def check(self):
        self.query = "SELECT BALANCE FROM customers_info WHERE USER_NAME = %s and PASS_WORD =%s"
        self.val = (self.name,self.password)
        self.mycursor.execute(self.query, self.val)
        self.x = self.mycursor.fetchone()
        self.b = list(self.x)
        for i in self.b:
            self.balance = int(i)
            time.sleep(1)
        print("Your balance is $" , self.balance)
        self.user = input("press 0 to go back: \n")
        if self.user == "0":
            self.operation()
        else:
            print("invalid input!")
            self.check()
    
    def signUp(self):
        print("sign up here")
        self.name = input("What is your full name: ")
        self.date = input("What is your date of birth: ")
        self.user = input("input your username: ")
        self.pw = input("input 4 digit password: ")
        self.phone = input("input your phone number: ")
        print(self.name + " thanks for banking with us.")
        self.balance = 0
        self.acctNumber = random.randrange(2000000000,2999999999)
        time.sleep(1)
        print("Your account number is " , self.acctNumber)
        self.mycursor = mycon.cursor()
        self.query = "INSERT INTO customers_info (FULLNAME, USER_NAME, PHONE_NUMBER, ACCT_NO, PASS_WORD) VALUES(%s, %s, %s, %s, %s)"
        val = (self.name, self.user, self.phone, self.acctNumber, self.pw)
        self.mycursor.execute(self.query, val)
        mycon.commit()
        self.user5 = input("press 0 to go back: \n")
        if self.user5 == "0":
            self.homePage()

at = atm()