![Python](https://img.shields.io/badge/python-%233776AB.svg?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%232496ED.svg?style=for-the-badge&logo=docker&logoColor=white)
![React](https://img.shields.io/badge/react-%2361DAFB.svg?style=for-the-badge&logo=react&logoColor=white)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Djoser](https://img.shields.io/badge/djoser-%23426AA5.svg?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/postgresql-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23F7DF1E.svg?style=for-the-badge&logo=javascript&logoColor=black)

# EUPHORIA - Магазин Духов

Добро пожаловать в магазин EUPHORIA - вашего проводника в мир ароматов и волшебства.

---

К проету подключена автоматическая документация Swagger:
```python
http://euphoriastore.hopto.org/api/swagger
```

Клонируем репозиторий:
```python
git@github.com:bebish/euphoria.git
```
### Устанавливаем зависимости 
```python
pip install -r requirements.txt
```
Заходим в рабочую директорию 
```python
cd infra/
```
### Заполняем файл .env вашими данными
```python
SECRET_KEY=<КЛЮЧ ПРОЕКТА>
DB_ENGINE=django.db.backends.postgresql
DB_NAME=<ИМЯ БАЗЫ ДАННЫХ>
POSTGRES_USER=<ИМЯ ПОЛЬЗОВАТЕЛЯ БД>
POSTGRES_PASSWORD=<ПАРОЛЬ>
DB_HOST=db
DB_PORT=5432
```
Далее поднимаем проект в режиме демона, делаем миграции и собираем статику:
```python
docker-compose up -d
docker-compose exec <имя_контейнера_бэкэнда> python3 manage.py makemigrations
docker-compose exec <имя_контейнера_бэкэнда> python3 manage.py migrate
docker-compose exec <имя_контейнера_бэкэнда> python3 manage.py collectstatic --noinput
```
Создаем администратора командой:
```python
docker-compose exec <имя_контейнера_бэкэнда> python manage.py createsuperuser
```
Проект доступен по домену:
```python
http://euphoriastore.hopto.org
```
---

## Проект готов к работе!
### *Авторы*

---

#### Доктурбаев Эраалы (teamlead)
#### Сосламбеков Амир
#### Шайымкулова Бегимай
#### Орунбаев Абдугани