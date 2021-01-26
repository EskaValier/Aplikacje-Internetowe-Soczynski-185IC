# Aplikacje-Internetowe-Soczynski-185IC

**1. Blog uruchomiony na PaaS**<br />

Uruchomioną stronę można znaleźć pod adresem: https://blog-soczynski.herokuapp.com/

instalacja pakietów i tworzenie projektu,<br />
korzystanie z serwera deweloperskiego,<br />
modele, migracje i ORM,<br />
ustawienia projektu,<br />
tworzenie superusera i panel admina,<br />
tworzenie aplikacji w Django,<br />
QuerySets i menadżery obiektów,<br />
praca z plikami views .py, urls .py i szablonami,<br />
praca z formularzmi (dodawanie posta, edycja istniejącego posta),<br />
blog umieszczamy na platfoformie typu PaaS (np. Heroku).

**2. Rejestracja użytkowników**

należy wykorzystać wbudowane widoki uwierzytelniające<br />
należy zrealizować następujące operacje:<br />
widoki ‘login’ i ‘logout’<br />
widok od zmiany hasła (PasswordChangeView)<br />
widok od resetu hasła (PasswordResetView)<br />

**3. Różne sposoby uwierzytelniania**
uwierzytelnianie przez social media i za pomocą wbudowanych backendów (username lub email),<br />
należy dodać dwa dowolne backendy uwierzytelniające do listy AUTHORIZATION_BACKENDS (np. Facebook i Twitter),<br />
konieczne będzie utworzenie aplikacji ww. portalach,<br />

**4. REST API z DRF**

- Django Rest Framework,
- zezwolenia,
- Swagger,
- serializery,

**5. Web Scraping**
- krótki wstęp do web scrapingu z Pythonem,
- krótki wstęp do web scrapingu z BS4,
- Beautiful Soup,
- XPath i lxml,
- implementacja wyszukiwania elementów do scrapowania za pomocą formularza w Django,

**6. Zezwolenia i uwierzytelnianie w DRF**
- viewsets,
- routers,
- uwierzytelnianie (basic, session, token),

**7. Python + Redis + Django**
- nie jest konieczna instalacja Redisa za pomocą Dockera, wystarczy standardowa instalacja,
- oprócz instalacji redis-server konieczna jest instalacja pakietu redis poprzez ‘pip’,
- najwygodniej jest podzielić się zadaniami, żeby przyspieszyć pracę z Redisem,
- tutorial o współpracy Python + Redis,
- do przerobienia przykład współpracy Django + Redis + Celery,
- praca z workerami w Celery,
- praca z Celery Beat,

**8. Czat z użyciem django-channels + Web Workers**

* **part I:**
- szybkie wyjaśnienie idei WebSockets,
- więcej szczegółów na javascript.info,
- modułws z Node.js,
- czym jest WSGI?,
- od Django 3.0 możemy również korzystać z zalet ASGI (Asynchronous Server Gateway Interface),
- gdzie można korzystać z ASGI,
- przykład z wykorzystaniem socket.io do budowy czata

* **part II:**
- wyjaśnienie idei stosowania Web Workerów,
- praca z Web Worker’ami,
- należy zwrócić uwagę na typowe dla Workerów elementy: event listener onmessage i funkcję postMessae(),
- należy wdrożyć dwa Web Workery, z których każdy wykonuje “czasochłonne” obliczenia, np. obliczanie liczby ciągu Fibonnaciego.

**9. Django + React (aplikacja CRUD)**
- backend napisany w Django,
- frontend napisany za pomocą React.js,
- biblioteka ‘axios’ użyta do “konsumowania” API wystawionego przez DRF,
- przykład aplikacji CRUD z wykorzystaniem Django i React’a,
- należy przeanalizować i wdrożyć kod z ww. poradnika,

**10. Django + React (aplikacja typu ToDo)**
- backend napisany w Django,
- frontend napisany za pomocą React.js,
- biblioteka ‘axios’ użyta do “konsumowania” API wystawionego przez DRF,
- przykład aplikacji To-Do z wykorzystaniem Django i React’a,
- należy przeanalizować i wdrożyć kod z ww. poradnika,
