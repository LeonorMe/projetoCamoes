# LEIM-Projeto-Camoes
Projeto final LEIM #60 A obra de Camões – divulgação multimédia

---

Python 3.13.3

django: https://www.djangoproject.com/

...> "setup envioment"
...> pip install django

Setup new project:
\newprojectname> django-admin startproject projetoCamoes
\newprojectname> cd projetoCamoes
\newprojectname\newprojectname> python manage.py startapp appname

Server:
python manage.py runserver
http://127.0.0.1:8000/


Databases:
(fazer sempre que se muda o "models.py)
...\myproject> python manage.py makemigrations
...\myproject> python manage.py migrate

python manage.py makemigrations mainPages
python manage.py sqlmigrate mainPages 0001
python manage.py shell
>>>> from mainPages.models import Quote
>>>> Quote.objects.all()
// Add a record to the table
quote = Quote(content='', author='', book='')
quote.save()
quote = Quote.objects.all()[0]
quote.delete()

Get administration credentials
for: http://127.0.0.1:8000/admin/login/?next=/admin/
...\myproject> python manage.py createsuperuser
Username: admin
Email address: (can skip)
Password: admin
Password (again): admin


Backup database
>> python manage.py archive


python manage.py collectstatic
https://www.geeksforgeeks.org/python/django-static-file/ 

---
Paginas de erro:
[x] 404 Page Not Found
[-] 500 Internet Server Error
[ ] 400 Bad Request
[ ] 403 Forbidden 
[ ] 503 Service Unavailable


---
Gunicorn
gunicorn myproject.wsgi


---
Coventios and best practices
https://medium.com/django-unleashed/django-project-structure-a-comprehensive-guide-4b2ddbf2b6b8
https://docs.djangoproject.com/en/4.2/misc/design-philosophies/

https://www.geeksforgeeks.org/python/handle-multiple-forms-on-a-single-page-in-django/
https://docs.djangoproject.com/en/4.2/ref/templates/api/#writing-your-own-context-processors

solved subscribe bug:
https://www.geeksforgeeks.org/python/python-form-validation-using-django/

permitions:
https://docs.djangoproject.com/en/5.2/topics/http/views/


## Language
django-admin makemessages -l en
//To reexamine all source code and templates for new translation strings and update all message files for all languages, run this:
django-admin makemessages -a 
// After you create your message file – and each time you make changes to it – you’ll need to compile it into a more efficient form
django-admin compilemessages

> -m pip install -r requirements.txt
> manage.py collectstatic --no-input
> manage.py migrate