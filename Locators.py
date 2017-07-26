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
    PASSWORD_BOX = (By.CLASS_NAME,"tooltip-inner")
    PASSWORD_RESET_BUTTON = (By.XPATH,"//*[@id=\"remindPassword\"]")

class PasswordPageLocators:
    NAME_FIELD_PASSWD=(By.NAME,"store_name")
    MAIL_FIELD_PASSWD=(By.NAME,"email")
    CONFIRM_BUTTON_PASSWD=(By.XPATH,"/html/body/section/form/button")

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

class AdminPanelLocators:

    ADD_BOX = (By.XPATH, "// *[ @ id = \"blankslateProductsHeading\"] / h4 / a")
    ADD_PRODUCT_BUTTON=(By.XPATH,"//*[@id=\"blankslateProducts\"]/div/div[2]/div/a[3]")

class ProductFormLocators:

    PRODUCT_NAME = (By.XPATH,"//*[@id=\"name\"]")
    PRODUCT_PRICE = (By.XPATH,"//*[@id=\"price\"]")
    PRODUCT_SKU = (By.NAME,"sku")
    PRODUCT_DESCRIPTION = (By.XPATH,"//*[@id=\"redactor-uuid-0\"]")
    SHORT_DESCRIPTION = (By.XPATH, "//*[@id=\"short_description\"]")
    SET_TAX = (By.XPATH,"//*[@id=\"tax\"]")
    WEIGHT = (By.NAME,"weight")
    WIDTH = (By.NAME,"width")
    HEIGHT = (By.NAME,"weight")
    DEPTH = (By.NAME,"depth")
    DIAMETER = (By.NAME,"diameter")
    DELIVERY = (By.XPATH,"/html/body/section[2]/section/section/article/section/section/form/table/tbody/tr[2]/td[2]/section[4]/div/label")
    TAG_TEXT = (By.ID,"tag")
    TAG_CONFIRM = (By.XPATH,"/html/body/section[2]/section/section/article/section/section/form/table/tbody/tr[3]/td[2]/section/section/button")
    IMAGE = (By.XPATH,"/html/body/section[2]/section/section/article/section/section/form/table/tbody/tr[4]/td[2]/ul/li[1]/a/input")
    BUY_EMPTY = (By.XPATH,"//*[@id=\"addToStockView\"]/section[2]/section[2]/div/label")
    META_TITLE = (By.NAME,"meta_title")
    META_DESCRIPTION = (By.NAME, "meta_description")
    SAVE_CHANGES = (By.XPATH, "/html/body/section[2]/section/section/article/section/section/form/section[3]/section/button")