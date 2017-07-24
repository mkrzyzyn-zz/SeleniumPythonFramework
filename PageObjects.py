from selenium import webdriver
from Locators import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import time
#driver = webdriver.Chrome()

class MainPage(object):

    def __init__(self,driver):
        self.driver=driver

    #Initialize
    def InitMain(self):
        self.driver.get("https://www.shoplo.pl/?home=n")
        self.driver.maximize_window()

    # Click Logowanie
    def ClickLogowanie(self):

        el = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((MainPageLocators.LOGOWANIE_BUTTON)))
        el.click()

    # Click Zaloguj do sklepu Shoplo
    def ClickZaloguj(self):

        el = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((MainPageLocators.ZALOGUJ_BUTTON)))
        el.click()

        return LogInWindow(self.driver)

class LogInWindow(object):

    def __init__(self,driver):
        self.driver=driver

    #Click Kliknij by się zarejestrować
    def ClickToRegister(self):

        el = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((LoginPageLocators.REGISTER_BUTTON)))
        el.click()
        return RegisterForm(self.driver)

    def FillInName(self):

        el = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((LoginPageLocators.NAME_FIELD)))
        el.send_keys("Testowy16")

    def FillInMail(self):
        el = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((LoginPageLocators.MAIL_FIELD)))
        el.send_keys("maciej.krzyzynski16@gmail.com")

    def FillInPassword(self):

        el = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((LoginPageLocators.PASSWORD_FIELD)))
        el.click()
        el.send_keys("maciej.krzyzynski@gmail.com")

    def ClickConfirm(self):
        el = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((LoginPageLocators.CONFIRM_BUTTON)))
        el.click()

class RegisterForm(object):

    def __init__(self,driver):
        self.driver=driver

    # Fill in name
    def FillInName(self):
        el = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((RegisterPageLocators.NAME_FIELD)))
        el.send_keys("Testowy16")

    def FillInMail(self):
        el = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((RegisterPageLocators.MAIL_FIELD)))
        el.send_keys("maciej.krzyzynski16@gmail.com")

    def FillInPassword(self):

        el = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((RegisterPageLocators.PASSWORD_FIELD)))
        el.click()
        el.send_keys("maciej.krzyzynski@gmail.com")

    def ClickConfirm(self):
        el = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((RegisterPageLocators.CONFIRM_BUTTON)))
        el.click()

class WelcomeWindow(object):

    def __init__(self,driver):
        self.driver=driver

    # Fill in name
    def FillInName(self):
        el = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((WelcomePageLocators.NAME_FIELD)))
        el.send_keys("Testowy1")

    def FillInPhone(self):
        el = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((WelcomePageLocators.PHONE_FIELD)))
        el.send_keys("600015545")

    def SelectCountry(self):

        el = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((WelcomePageLocators.COUNTRY_SELECT)))
        el.click()
        el = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((WelcomePageLocators.COUNTRY_1)))
        el.click()

    def SelectProducts(self):

        el = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((WelcomePageLocators.PRODUCTS_SELECT)))
        self.driver.execute_script("return arguments[0].scrollIntoView();", el)
        el.click()
        el = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((WelcomePageLocators.PRODUCT_1)))
        el.click()

    def SelectReason1(self):

        el = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((WelcomePageLocators.REASON1_SELECT)))
        el.click()
        el = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((WelcomePageLocators.REASON1_1)))
        el.click()


    def SelectReason2(self):

        el = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((WelcomePageLocators.REASON2_SELECT)))
        el.click()
        el = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((WelcomePageLocators.REASON2_1)))
        el.click()

    def ClickConfirm(self):
        el = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((WelcomePageLocators.CONFIRM_BUTTON)))
        el.click()



#Close
#driver.close()

