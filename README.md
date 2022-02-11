Selenium Python tests

Folder projektu zawiera:

1. Scenariusz testów kalkulatora, plik w formacie docx.
2. Testy akceptacyjne JsonPlaceholder REST API, plik w formacie json
3. Testy akceptcyjne Shoplo.pl, pozostałe pliki, uruchomienie przez Run.py.
   Możliwe są następujące scenariusze testowe:
   a. Utworzenie nowego konta użytkownika.
   b. Logowanie z poprawnymi danymi.
   c. Logowanie z niepoprawnymi danymi.
   d. Dodanie produktu po poprawnym logowaniu.

UWAGI

ad. 2

JsonPlaceholder API nie udostępnia metod POST, DELETE dla endpointu /COMMENTS

ad. 3

Dla ujednolicenia stosowano wyszukiwanie po XPath. Z uwagi na wydajność, tam gdzie możliwe, stosowano wyszukiwanie po unikalnych selektorach CSS
