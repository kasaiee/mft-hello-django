اولین جلسه کلاس پایتون

ابتدا با دستور یک محیط ایزوله به نام env ایجاد کردیم

```
python -m venv env
```

بعد با دستور زیر محیط ایزوله مون رو فعال کردیم

env\Scripts\activate

دقت کنید که باید اسم محیط ایزوله حتما داخل یک پرانتز اول خط اومده باشه وگرنه مشکل داریم

بعد با دستور زیر جنگو رو نصب کردیم

pip install django

بعد با دستور زیر اولین پروژه جنگویی مون رو ساختیم

```
python manage.py startproject hello_django
```

بعد با دستور زیر رفتیم داخل پوشه پروژه

cd hello_django

بعد با دستور زیر سرور رو ران کردیم

```
python manage.py runserver
```

بعد با دستور زیر مایگریت های اولیه رو انجام دادیم تا بتونیم سوپر یوزر درست کنیم

```
python manage.py migrate
```

بعد با دستور زیر سوپر یوزر درست کردیم

```
python manage.py createsuperuser
```

بعد با دستور زیر اولین اپ مون رو ساختیم

```
python manage.py startapp app_1
```

سپس بعد از اینکه مدل مون رو تغییر دادیم با دستور زیر میک مایگریشن کردیم

```
python manage.py makemigrations
```

و بعد با دستور زیر تغییرات رو در دیتابیس نهایی کردیم

```
python manage.py migrate
```
