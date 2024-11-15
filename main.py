#biblioteki
import openai
import os
import requests

#wczytanie klucza openai z zmiennych środowiskowych
openai.api_key = os.getenv("OPENAI_API_KEY")

#podanie adresu url z tekstem do zmiennej
url= "https://cdn.oxido.pl/hr/Zadanie%20dla%20JJunior%20AI%20Developera%20-%20tresc%20artykulu.txt"

#pobranie zmiennej z adresem url do zapytania dla openai
response = requests.get(url)

#sprawdza czy żądanie zakończyło się sukcesem i pobrało plik
if response.status_code == 200:
  text_content = response.text

#jeśli nie
else:
  print("Nie pobrało pliku")
  exit()

#wiadomości informujące chat o jego zachowaniu i zadaniach
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": f"Jesteś asystentem do korekty tekstu"},
    {"role": "user", "content": f"Odczytaj zawartość pliku:\n\n{text_content}\n\n popraw ją a wynik zapisz w pliku artykul.html."
                                f"Zastosuj tagi <img src="" tutaj wpisz image_placeholder.jpg, alt=""tutaj podaj szczegółowo jaki obraz wygenerwałeś> w miejscach w których powinny być obrazy."
                                f"Do każdego <img src"", alt=""> zastosuj tagi <figure> oraz <figcaption>."
                                f"Artykuł zapisz wyłącznie pomiędzy tagami <body> i </body>, nie dodawaj tagów takich jak <html>,</html>,<head>,</head>."
                                f"Upewnij się że każde miejsce w którym ma znaleźć się obraz jest odpowiednio oznaczone."
                                f"Nie pomijaj ostatniego zdania"
                                f"Zastosuj odpowiednią strukturę HTML, w tym <h1>, <p>, <br> "
                                f"Usuń wszystko poza <body></body>"}
  ],
#maksymalna ilość jednostek testowych jaka została przydzielona temu zapytaniu
  max_tokens=4096,
#parametr wpływający na losowość otrzymanych rezultatów
  temperature=0.9
)

#pobranie odpowiedzi z openai
html_content = response['choices'][0]['message']['content']
print(html_content)

#zapis do pliku html
with open("artykul.html", "w", encoding="utf-8") as file:
  file.write(html_content)
#////////////////////////zadanie dla chętnych////////////////////////////////
#tworzenie pustego szablonu strony html
response2 = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": f"Utwórz nowy plik o nazwie szablon.html"
                                    f"Dodaj stylizację css dla <p>,<h1>,<img src>,<figure>,<figcaption> nie zmieniaj koloru"
                                    f"Dodaj skrypt js informujący o załadowaniu strony"
                                    f"Sekcja body ma być pusta"
                                    f"Nie wypisuj co dodałeś/wygenerowałeś"}
      ],
  #maksymalna ilość jednostek testowych jaka została przydzielona temu zapytaniu
    max_tokens=4096,
  #parametr wpływający na losowość otrzymanych rezultatów
    temperature=0.9
)
#pobranie wygenerowanego szablonu od openai
html_content2 = response2['choices'][0]['message']['content']
print(html_content2)

#zapis szablonu do pliku html
with open("szablon.html", "w", encoding="utf-8") as file:
    file.write(html_content2)