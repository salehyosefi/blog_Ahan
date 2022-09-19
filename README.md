# وبلاگ آهن آلات
در این پروژه مدیر با ورود به پنل مدیریت امکان پست، ویرایش و حذف پست ها در وبلاگ را دارد.

## Technologies used
- [Python 3.8](https://www.python.org/) - Programming Language
- [Django](https://docs.djangoproject.com/en/4.0/releases/4.0/) - Web Framework
- [MySQL](https://www.mysql.com/) - Database
- [Git](https://git-scm.com/doc) - Version Control System
- [HTML5](https://www.w3.org/html/) - fundamental markup language


## Setup

Then setup env using the following command
```
python -m venv venv
```
Activate env with the following command
```
venv/Scripts/activate
```
Install requirements
```
pip install -r requirements.txt
```
Create a development database:
```
python manage.py migrate
```
If everything is alright, you should be able to start the Django development server:
```
python manage.py runserver
```
