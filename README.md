# DJANGO_PITE_PROJECT

[Link do wdrożenia](http://krzysztofstachanczyk.pythonanywhere.com/)

Wszystkie pliki projektu znajdują się w katalogu myEnv. 

## Wersje oprogramowania:
- python 3.4 
- django 1.8
- python-dateutil 
```
pip install python-dateutil
```
- django-picklefield-0.3.2 ( nie wymaga instalacji jest w katalogu projektu )

## Lista zadań do wykonania:
- ogólna struktura bazy danych - OK
- layout strony - OK
- logowanie i wylogowywanie - OK
- rejestracja - OK
- tworzenie i edycja ankiet - OK (integralność zachowana przez sprawdanie kluczy )
- dodawanie i ewentualna modyfikacja odpowiedzi - OK
- panel do zarządzania ankietami dla usera - OK
- tworzenie i wysyłanie raportów o odpowiedziach
- statystyki ( dla całej witryny i userów - googleChart może się przydać ) - im więcej tym lepiej
- ewentualna integracja ze stronami zewnętrznymi (googlecalendar ?)
- możliwość generowania arkuszy Excella z odpowiedziami (najszybciej będzie przy pomocy formatu CSV) 
- wysyłanie zbiorczego maila do członków ankiety
- testy
- generowanie raportów (może by się udało w PDF ? jak nie to w sposób taki aby ławo było je wydrukować ) wygląda przystępnie -[latex and django](https://blog.sevenbyte.org/2014/09/23/generating-pdfs-with-django-and-latex.html) 
- ulepszenie front-end (np chowanie się potwierdzeń poprawności zapisu do bazy danych po najechaniu #jqery itp )
- inne dodatki
