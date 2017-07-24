import PageObjects
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test(object):

    # Superclass driver instance variable initialization and initial configuration
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(0)

class CreateAccountTest(Test):

    def GoToLoginForm(self):

        main_page = PageObjects.MainPage(self.driver)
        main_page.InitMain()
        main_page.ClickLogowanie()
        main_page.ClickZaloguj()

    def GoToRegistrationForm(self):

        login_page = PageObjects.LogInWindow(self.driver)
        login_page.ClickToRegister()

    def FillInRegistrationForm(self):

        registration_page =  PageObjects.RegisterForm(self.driver)
        registration_page.FillInName()
        registration_page.FillInMail()
        registration_page.FillInPassword()
        registration_page.ClickConfirm()

    def FillInWelcomeForm(self):

        welcome_window = PageObjects.WelcomeWindow(self.driver)
        welcome_window.FillInName()
        welcome_window.FillInPhone()
        welcome_window.SelectCountry()
        welcome_window.SelectProducts()
        welcome_window.SelectReason1()
        welcome_window.SelectReason2()
        welcome_window.ClickConfirm()

class LoginTest(Test):

    def GoToLoginForm(self):

        main_page = PageObjects.MainPage(self.driver)
        main_page.InitMain()
        main_page.ClickLogowanie()
        main_page.ClickZaloguj()

    def FillInLoginForm(self):

        login_page = PageObjects.LogInWindow(self.driver)
        login_page.FillInName()
        login_page.FillInMail()
        login_page.FillInPassword()
        login_page.ClickConfirm()