import PageObjects
import Locators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions, Chrome


class Test(object):

    # Superclass driver instance variable initialization and initial configuration
    def __init__(self):

        opts = ChromeOptions()
        opts.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(chrome_options=opts)

        #self.driver = webdriver.Chrome()
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

    def FillInRegistrationForm(self,name,mail,password):

        registration_page =  PageObjects.RegisterForm(self.driver)
        registration_page.FillInName(name)
        registration_page.FillInMail(mail)
        registration_page.FillInPassword(password)
        registration_page.ClickConfirm()

    def FillInWelcomeForm(self):

        welcome_window = PageObjects.WelcomeWindow(self.driver)
        welcome_window.FillInName()
        welcome_window.FillInPhone()
        welcome_window.SelectCountry()
        welcome_window.SelectProducts()
        welcome_window.SelectReason1()
        welcome_window.SelectReason2()

        admin_panel = welcome_window.ClickConfirm()

        return admin_panel

class LoginTest(Test):

    def GoToLoginForm(self):

        main_page = PageObjects.MainPage(self.driver)
        main_page.InitMain()
        main_page.ClickLogowanie()
        main_page.ClickZaloguj()

    def FillInLoginFormExpectingSuccess(self,name,mail,password):

        login_page = PageObjects.LogInWindow(self.driver)
        login_page.FillInName(name)
        login_page.FillInMail(mail)
        login_page.FillInPassword(password)
        admin_panel = login_page.ClickConfirm()

        assert login_page.isTitleMatches("Shoplo - testowy16")

        return admin_panel

    def FillInLoginFormExpectingFailure(self,name,mail,password):

        login_page = PageObjects.LogInWindow(self.driver)
        login_page.FillInName(name)
        login_page.FillInMail(mail)
        login_page.FillInPassword(password)
        login_page.ClickConfirm()

        assert login_page.isElementPresent(Locators.LoginPageLocators.PASSWORD_BOX)

    def ClickForgotPassword(self):

        login_page = PageObjects.LogInWindow(self.driver)
        login_page.ClickPasswordReset()

    def FillPasswordForm(self):

        password_reset_page = PageObjects.PasswordResetWindow(self.driver)
        password_reset_page.FillName()
        password_reset_page.FillMail()
        password_reset_page.ClickConfirm()

class AddProductTest(object):


    def __init__(self,admin_panel):
        self.admin_panel=admin_panel


    def GoToProductForm(self):

        #admin_panel = PageObjects.AdminPanel(self.driver)
        self.admin_panel.SelectAddBox()
        product_form = self.admin_panel.ClickAddProduct()

        return product_form

    def FillInProductForm(self,product_form):

        product_form.FillProductName()
        product_form.FillProductPrice()
        product_form.FillSku()
        product_form.FillProductDescription()
        product_form.FillShortDescription()
        product_form.AddTax()
        product_form.AddParameters()
        product_form.SelectDelivery()
        product_form.AddTag()
        product_form.AddImage()
        product_form.BuyIfEmpty()
        product_form.AddMetaTitle()
        product_form.AddMetaDescription()
        product_form.ClickSaveChanges()



