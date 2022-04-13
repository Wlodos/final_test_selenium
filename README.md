# final_test_selenium

Тестовые сценарии проверяют кликабельность и поведение элементов главной страницы и страницы авторизации сайта labirint.ru.
Для работы требуются библиотеки: pytest, pytest-selenium.
Для запуска тестов главной страницы -  python -m pytest -v --driver Chrome --driver-path /chromedriver.exe tests/test_home_page.py
Для запуска тестов страницы авторизации  python -m pytest -v --driver Chrome --driver-path /chromedriver.exe tests/test_auth_page.py
Также каждый из тестов можна запускать отдельно, нажатием кнопки "плей" напротив теста в PyCharm.
