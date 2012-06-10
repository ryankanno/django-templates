# django-templates

** Here be dragons **

Just a small Django app to get the latest and greatest base templates.

Features 
--------

Supports:

* [HTML5 Boilerplate 3.0](http://html5boilerplate.com)

Install
-------

Clone this project somewhere your Python path can find it.

Add django-templates to INSTALLED_APPS

    INSTALLED_APPS = (
        ...
        'django-templates',
        ...
    )


Usage
-----

To use django-templates, just extend the various base layouts. 

    {% extends 'html5boilerplate/base.html' %}

    {% block header.content %}
        Helllllo World.
    {% endblock header.content %}
