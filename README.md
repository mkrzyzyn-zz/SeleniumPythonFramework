Folder projektu zawiera:

1. Scenariusz testów kalkulatora, plik w formacie docx.
2. Testy akceptacyjne JsonPlaceholder REST API, plik w formacie json
3. Testy akceptcyjne Shoplo.pl, pozosta³e pliki, uruchomienie przez Run.py.
   Mo¿liwe s¹ nastêpuj¹ce scenariusze testowe:
   a. Utworzenie nowego konta u¿ytkownika.
   b. Logowanie z poprawnymi danymi.
   c. Logowanie z niepoprawnymi danymi.
   d. Dodanie produktu po poprawnym logowaniu.

UWAGI

ad. 2

JsonPlaceholder API nie udostêpnia metod POST, DELETE dla endpointu /COMMENTS

ad. 3

Dla ujednolicenia stosowano wyszukiwanie po XPath. Z uwagi na wydajnoœæ, tam gdzie mo¿liwe, stosowano wyszukiwanie po unikalnych selektorach CSS
