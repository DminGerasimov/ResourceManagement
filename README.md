# В проекте использованs Django==4.1.2 + Postgersql 15.0

Скрипт реляционной БД не предоставлен, т.к. схема создается
на этапе запуска контейнера веб-сервиса путем миграций моделей
приложения.

Конфиг приложения находится в файле .env.dev


Для запуска сервиса backend'a в Ubuntu > 20.04 необходимо установить Docker и Docker Compose
и Docker Compose.
Затем клонировать репозитарий в текущую папку
```
cd ~
git clone https://github.com/DminGerasimov/ResourceManagement
cd ResourceManagement
chmod +x ./entrypoint.sh
sudo docker-compose up -d -- build
```

После запуска контейнеров, сервис доступен по IP адресу выше указанной 
Linux операционной системы на порту 8000.

Перейдя по адресу IP:8000/v1/auth/register
 и используя браузер Mozilla FFox в режиме Raw data выполнить  POST запрос с 
 тестовыми данными:
 ```
 {
    "phone": "+79167003020",
    "login": "rubella19",
    "password": "1Qwerty!",
    "name": "Анастасия",
    "birth": "2000-07-28",
    "tg": "@Rubella19",
    "email": "anastasia.a.krasnova@gmail.com"
}
```
В ответ получть id пользователя из базы данных.


Аналогично проверить endpoint IP:8000/v1/auth/login c данными:
```
{
    "login": "rubella19",
    "password": "1Qwerty!",
}
```
В ответ получть id пользователя из базы данных.

Перейдя на endpoint IP:8000/v1/user?id=1

В ответ получть данные пользователя из базы данных (кроме пароля).

При неверных query-параметрах - вывод ошибки.


