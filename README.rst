=============
Django Stisla
=============

Django Stisla is a Bootstrap 4 based admin template for Django admin interface developed using the `stisla <https://github.com/stisla/stisla>`_ free bootstrap admin template.

Installation
------------

Install the package from PyPi::

    pip install django-stisla
         

Quick start
-----------

1. Add "django_stisla.apps.admin" with "django.contrib.admin" & "django.contrib.auth" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django_stisla.apps.admin',
        'django.contrib.admin',
        'django.contrib.auth',
        ...
    ]

2. Make sure django.template.context_processors.request is enabled in project settings.py::

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    ...
                    'django.template.context_processors.request',
                    ...
                ],
            },
        },
    ]

3. Include the admin URLconf in your project urls.py like this::
    
    ...
    from django_stisla import admin
    ...
    urlpatterns = [
        ...
        path('admin/', admin.site.urls),
        ...
    ]


4. You can set following theme configurations in URLconf::

    ...
    admin.site.site_header = "Django administration"
    admin.site.site_title = "Django site admin"
    admin.site.index_title = "Site administration"
    admin.site.site_short_title = "DJ"
    ...

5. Start the development server and visit http://127.0.0.1:8000/admin/ to see your newly installed Django Stisla for admin.