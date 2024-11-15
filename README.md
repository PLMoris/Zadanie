Aplikacja napisana w języku Python, pobiera klucz API OpenAI, następnie łączy się z chatem w wersji "gpt-3.5-turbo".
Następnie wysyła zapytanie do OpenAI, informując je jaką rolę pełni, oraz przekazuje mu zadanie.
Zadaniem jest odczytanie tekstu z adresu URL, skorygowanie go do poprawnej formy. A następnie zapisanie rezultatu w pliku artykul.html
Chat ma za zadanie utworzyć plik .html w którym nie będzie nic poza sekcją <body> w której zapisany zostanie poprawiony tekst.
Dodatkowym zadaniem jest wstawienie potencjalnych obrazów z podpisami w odpowiednich miejscach tekstu.
Każde zdjęcie osadzone zostało w tagu "figure" z podpisem oraz tagiem "alt".
Program dodatkowo wysyła zapytanie do OpenAI aby utworzyło szablon z pustą sekcją <body>, stylistyką CSS, i prostym kodem JS.
Utworzony został także plik podglad.html, do którego można wkleić kod artykułu do sekcji <body> co pozwoli na przeglądanie artykułu.

Aby uruchomić program należy załadować go do PyCharm, w zmiennych środowiskowych podać swój klucz do API, i uruchomić kompilator.
