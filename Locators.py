from selenium.webdriver.common.by import By

class  MainPageLocators:
    LOGOWANIE_BUTTON = (By.XPATH, "//*[@id=\"mm-0\"]/header/div/div[2]/nav/ul/li[6]/ul/li/span")
    ZALOGUJ_BUTTON = (By.XPATH, "//*[@id=\"mm-0\"]/header/div/div[2]/nav/ul/li[6]/ul/li/div/div/div/ul/li[1]/a/span[2]")

class LoginPageLocators:
    REGISTER_BUTTON=(By.XPATH, "/html/body/section/form/p[3]/a")
    NAME_FIELD=(By.XPATH, "//*[@id=\"storeName\"]")
    PASSWORD_FIELD=(By.XPATH,"//*[@id=\"fieldset_password\"]/div[1]/input")
    MAIL_FIELD=(By.XPATH,"//*[@id=\"fieldset_email\"]/div/input")
    CONFIRM_BUTTON = (By.CSS_SELECTOR, "body > section > form > button")

class RegisterPageLocators:
    NAME_FIELD=(By.XPATH, "//*[@id=\"storeName\"]")
    MAIL_FIELD=(By.XPATH, "//*[@id=\"storeEmail\"]")
    PASSWORD_FIELD=(By.XPATH, "//*[@id=\"storePassword\"]")
    CONFIRM_BUTTON=(By.CSS_SELECTOR, "#registerShop > button")

class WelcomePageLocators:
    NAME_FIELD=(By.XPATH, "//*[@id=\"fieldset_name\"]/div/input")
    PHONE_FIELD=(By.XPATH, "//*[@id=\"fieldset_phone\"]/div/input")
    COUNTRY_SELECT=(By.XPATH, "/html/body/section/form/fieldset[3]/div/button")
    PRODUCTS_SELECT=(By.XPATH, "//*[@id=\"fieldset_selling\"]/div/button/span[1]")
    REASON1_SELECT=(By.XPATH, "//*[@id=\"fieldset_why\"]/div/button")
    REASON2_SELECT=(By.XPATH, "//*[@id=\"fieldset_hear\"]/div/button")
    CONFIRM_BUTTON=(By.XPATH, "/html/body/section/form/section[2]/section/button")
    COUNTRY_1=(By.XPATH,"/html/body/section/form/fieldset[3]/div/div/ul/li[3]")
    PRODUCT_1=(By.XPATH,"//*[@id=\"fieldset_selling\"]/div[2]/div/ul/li[3]/a/span[1]")
    REASON1_1=(By.XPATH,"//*[@id=\"fieldset_why\"]/div[2]/div/ul/li[3]/a/span[1]")
    REASON2_1=(By.XPATH,"//*[@id=\"fieldset_hear\"]/div[2]/div/ul/li[2]/a")
