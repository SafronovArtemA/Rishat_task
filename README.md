Rishat_task

Протестировать решение можно по ссылке:
https://artemsafronov.pythonanywhere.com/item/1


Для проверки на локальном хосте:

Перейти в проект выполнив команду:
cd shop

Создать .env и добавить переменную API_KEY с ключом для тестового режима платежной сиситемы stripe.com

В виртуальном окружении выполнить команду:
pip install -r requirements.txt

Далее запустить сервер командой:
python manage.py runserver

Перейти по адресу:
http://localhost:8000/item/1
