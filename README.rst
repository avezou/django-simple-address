====
Simple-Address
=====

Simple-Address is a simple Django app to save US addresses (it can
potentially be used for others). It does not provide a front end.
The intent of this is to be used on the admin site for invoicing
purposes (and potentially others).

Quick start
-----------
1. Pre-requisite:
    Make sure django-localflavor is installed and added to your INSTALLED_APPS

2. Install with pip install django-simple-address

3. Add "simple-address" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'address',
    ]


4. Run `python manage.py migrate` to create the address models.

5. Start the development server and visit http://127.0.0.1:8000/admin/
   to create addresses (you'll need the Admin app enabled).

6. TODO: Add testing and frontend access.
