import TestCases as TC

# Program wykonuje się przez uruchomienie metody run_suite()
# Jej pod-funkcje odpowiadają różnym testom, można je łączyć w celu testowania różnych ścieżek wykonania


def run_suite():

    #admin_panel=create_account_test()
    #login_test_failure()
    #login_test_reset_password()
    admin_panel=login_test_success()
    add_product_test(admin_panel)

#Odkomentuj, by utworzyć nowe konto użytkownika na dane Testowy17, maciej.krzyzynski17@gmail.com, maciej.krzyzynski@gmail.com

def create_account_test():

    create_account_test = TC.CreateAccountTest()
    create_account_test.GoToLoginForm()
    create_account_test.GoToRegistrationForm()
    create_account_test.FillInRegistrationForm("Testowy17", "maciej.krzyzynski17@gmail.com","maciej.krzyzynski@gmail.com")
    admin_panel=create_account_test.FillInWelcomeForm()
    return admin_panel

# Test logowania na konto użytkownika na powyższe dane

    # Expected: success

def login_test_success():

    login_test = TC.LoginTest()
    login_test.GoToLoginForm()
    admin_panel=login_test.FillInLoginFormExpectingSuccess("Testowy16", "maciej.krzyzynski16@gmail.com", "maciej.krzyzynski@gmail.com")
    return admin_panel

    # Expected: failure

def login_test_failure():

    login_test = TC.LoginTest()
    login_test.GoToLoginForm()
    login_test.FillInLoginFormExpectingFailure("test","test@test.com","test")

def add_product_test(admin_panel):

    add_product_test = TC.AddProductTest(admin_panel)
    product_form=add_product_test.GoToProductForm()
    add_product_test.FillInProductForm(product_form)



def login_test_reset_password():

    login_test = TC.LoginTest()
    login_test.GoToLoginForm()
    login_test.ClickForgotPassword()
    login_test.FillPasswordForm()

run_suite()