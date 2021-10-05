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

1. Add "django_stisla.apps.admin" and "widget_tweaks" with "django.contrib.admin" & "django.contrib.auth" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django_stisla',
        'django.contrib.admin',
        'django.contrib.auth',
        ...
        'widget_tweaks'
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


Admin Model Registration
------------------------

To register your models in Django admin, please import "from django_stisla.admin" in your applications admin.py and register your models as follows::

    ...
    from django_stisla.admin import site
    ...
    ...
    site.register(Image)
    site.register(Author)
    site.register(Topic)
    ...


Theme Customizations
--------------------

To set logo/title in admin login page, please create templates/admin/login.html file in your application and use the following code::

    {% extends "admin/login.html" %}

    {% block login-brand %}
    <div class="login-brand">
        <h1>Django Administration</h1>
    </div>
    {% endblock %}


To add extra CSS to dashboard theme, create static/admin/assets/css/extra.css file in your app. For example you can customize Font-awesome icons in the sidebar menu as follows based on your loaded apps in django::

    /* Custom font awesome icon for django auth app */

    .fa-auth:before { 
        content: "\f023";
    }

    /* Custom font awesome icon for an app name cms */

    .fa-cms:before {
        content: "\f0ad";
    }

    /* Custom font awesome icon for an app name order */

    .fa-order:before {
        content: "\f07b";
    }
