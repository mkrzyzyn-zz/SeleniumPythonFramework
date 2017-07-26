from selenium import webdriver
from Locators import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

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

    def FillInName(self,name):

        el = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((LoginPageLocators.NAME_FIELD)))
        el.send_keys(name)

    def FillInMail(self,mail):
        el = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((LoginPageLocators.MAIL_FIELD)))
        el.send_keys(mail)

    def FillInPassword(self,password):

        el = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((LoginPageLocators.PASSWORD_FIELD)))
        el.click()
        el.send_keys(password)

    def ClickConfirm(self):

        el = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((LoginPageLocators.CONFIRM_BUTTON)))
        el.click()

        return AdminPanel(self.driver)

    def isTitleMatches(self,title):

        return title in self.driver.title

    def isElementPresent(self,locator):

        return WebDriverWait(self.driver,10).until(EC.presence_of_element_located((locator)))

    def ClickPasswordReset(self):

        el = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((LoginPageLocators.PASSWORD_RESET_BUTTON)))
        el.click()

class PasswordResetWindow(object):

    def __init__(self,driver):
        self.driver=driver

    def FillName(self):
        el = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((PasswordPageLocators.NAME_FIELD_PASSWD)))
        el.send_keys("Testowy16")

    def FillMail(self):
        el = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((PasswordPageLocators.MAIL_FIELD_PASSWD)))
        el.send_keys("maciej.krzyzynski16@gmail.com")

    def ClickConfirm(self):

        el = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((PasswordPageLocators.CONFIRM_BUTTON_PASSWD)))
        el.click()

class RegisterForm(object):

    def __init__(self,driver):
        self.driver=driver

    # Fill in name
    def FillInName(self,name):
        el = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((RegisterPageLocators.NAME_FIELD)))
        el.send_keys(name)

    def FillInMail(self,mail):
        el = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((RegisterPageLocators.MAIL_FIELD)))
        el.send_keys(mail)

    def FillInPassword(self,password):

        el = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((RegisterPageLocators.PASSWORD_FIELD)))
        el.click()
        el.send_keys(password)

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

        return AdminPanel(self.driver)

class AdminPanel(object):

    def __init__(self,driver):
        self.driver=driver

    def SelectAddBox(self):

        el = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AdminPanelLocators.ADD_BOX)))
        el.click()

    def ClickAddProduct(self):

        #builder = ActionChains(self.driver)

        el = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AdminPanelLocators.ADD_PRODUCT_BUTTON)))
        el.click()

        return ProductForm(self.driver)

class ProductForm(object):

    def __init__(self,driver):
        self.driver=driver

    def FillProductName(self):

        el = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((ProductFormLocators.PRODUCT_NAME)))
        el.send_keys("Produkt")

    def FillProductPrice(self):

        el = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((ProductFormLocators.PRODUCT_PRICE)))
        el.send_keys("100")

    def FillSku(self):

        el = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((ProductFormLocators.PRODUCT_SKU)))
        el.send_keys("10")

    def FillProductDescription(self):

        el = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((ProductFormLocators.PRODUCT_DESCRIPTION)))
        self.driver.execute_script("return arguments[0].scrollIntoView();", el)
        el.send_keys("ABC")

    def FillShortDescription(self):

        el = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((ProductFormLocators.SHORT_DESCRIPTION)))
        self.driver.execute_script("return arguments[0].scrollIntoView();", el)
        el.send_keys("short ABC")

    def AddTax(self):

        el = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((ProductFormLocators.SET_TAX)))
        self.driver.execute_script("return arguments[0].scrollIntoView();", el)
        el.send_keys("15")

    def AddParameters(self):

        el = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((ProductFormLocators.WEIGHT)))
        el.send_keys("1")

        el = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((ProductFormLocators.WIDTH)))
        el.send_keys("10")

        el = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((ProductFormLocators.HEIGHT)))
        el.send_keys("10")

        el = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((ProductFormLocators.DEPTH)))
        el.send_keys("10")

        el = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((ProductFormLocators.DIAMETER)))
        self.driver.execute_script("return arguments[0].scrollIntoView();", el)
        el.send_keys("10")

    def SelectDelivery(self):

        el = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((ProductFormLocators.DELIVERY)))
        el.click()

    def AddTag(self):

        el = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((ProductFormLocators.TAG_TEXT)))
        el.send_keys("TAG")

        el = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((ProductFormLocators.TAG_CONFIRM)))
        el.click()

    def AddImage(self):

        el = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((ProductFormLocators.IMAGE)))
        el.send_keys("C:\img.jpg")
        self.driver.execute_script("return arguments[0].scrollIntoView();", el)

    def BuyIfEmpty(self):

        el = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((ProductFormLocators.BUY_EMPTY)))
        el.click()
        self.driver.execute_script("return arguments[0].scrollIntoView();", el)

    def AddMetaTitle(self):
        el = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((ProductFormLocators.META_TITLE)))
        el.send_keys("123")

    def AddMetaDescription(self):

        el = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((ProductFormLocators.META_DESCRIPTION)))
        el.send_keys("456")

    def ClickSaveChanges(self):

        el = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((ProductFormLocators.SAVE_CHANGES)))
        el.click()

#Close
#driver.close()

