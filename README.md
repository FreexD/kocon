# Kocon

## Konfiguracja środowiska

Przedstawiony opis konfiguracji zakłada pracę na systemie Windows. W sytemie Linux kroki mogą się lekko różnić, ale nie powinny sprawić problemu.

##### Instalacja narzędzi
* python2.7 [(link)][python]
* pip  [(link)][pip]
* konsola git [(link)][git] [opcjonalne]
* django, poleceniem:

> pip install django

* virtualenv, poleceniem:

> pip install virtualenv

> pip install virtualenvwrapper-powershell

##### Konfiguracja plików

W katalogu głównym, po zaimportowaniu projektu należy stworzyć wirtualnie środowisko do pracy w django:

> virtualenv venv

Następnie aktywujemy je:

> venv/Scripts/activate

Oraz instalujemy wszystkie potrzebne pakiety do pracy z naszym projektem:

> pip install -r requirements.txt

Po zakończonej pracy opuszczamy środowisko poleceniem:

> deactivate

## Użycie

##### Polecenia

* uruchomienie serwera aplikacji django lokalnie ( domyślnie localhost:8000 )
    > python manage.py runserver <port> | <ip:port>
* uruchomienie testów jednostkowych
    > python manage.py test
* zmigrowanie bazy danych jeżeli były w niej jakieś zmiany
    > python manage.py migrate

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

[python]: <https://www.python.org/downloads/>
[pip]: <https://pip.pypa.io/en/latest/installing/>
[git]: <https://git-for-windows.github.io/>
