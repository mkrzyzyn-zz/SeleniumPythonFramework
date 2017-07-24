import TestCases as TC

# Test utworzenia konta użytkownika na dane testowy16, maciej.krzyzynski16@gmail.com
#create_account_test = TC.CreateAccountTest()
#create_account_test.GoToLoginForm()
#create_account_test.GoToRegistrationForm()
#create_account_test.FillInRegistrationForm()
#create_account_test.FillInWelcomeForm()

# Test logowania na konto użytkownika na powyższe dane

login_test = TC.LoginTest()
login_test.GoToLoginForm()
login_test.FillInLoginForm()

