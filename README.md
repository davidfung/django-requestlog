django-requestlog
=================

A Django middleware to log incoming request to a database.  The logs
are available in the Django admin site.

Installation
------------

In settings.py

    INSTALLED_APPS = (
        ...
        'requestlog',
    )

    MIDDLEWARE_CLASSES = (
        ...
        'requestlog.middleware.RequestLogMiddleware',
    )

    # optionally specify exclusion, e.g. admin site
    REQUESTLOG_EXCLUDE_PATH_PREFIX = (
        '/admin/',
        '/favicon.ico',
    )

Create the model tables

   $ python manage.py syncdb



