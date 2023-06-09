# m3 project
### Это небольшой проект на m3, реализующий интерфейсы (приложения) для полного CRUD взаимодействия с Django моделями User, Permission, ContentType и Group.
---
# Installation
---
## Dev
### Для установки данного проекта нужно пройтись по нескольким пунктам:
### - (опционально) Создать виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate
```
### - Установить все зависимости из requirements.txt:
```bash
pip install -r requirements.txt
```
### - Перейти в каталог m3_project, запустить миграции базы данных, а также сам сервер:
```
cd m3_project
python manage.py migrations
python manage.py runserver
```
---
## Production
### Создать виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate
```
### Установить проект через pip:
```bash
pip install https://github.com/NikitolProject/m3_project.git \
 --extra-index-url http://pypi.bars-open.ru/simple/ \
 --trusted-host pypi.bars-open.ru
```
### Запустить миграцию базы данных и сам сервер:
```
python <путь_к_вашему_окружению>/lib/python3.6/site-packages/m3_project/manage.py migrations
python <путь_к_вашему_окружению>/lib/python3.6/site-packages/m3_project/manage.py runserver
```

