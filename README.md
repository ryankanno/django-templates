django-templates
================

** Here be dragons **

Just a small Django app to get the latest and greatest base templates.

Supports:

* [HTML5 Boilerplate](http://html5boilerplate.com)

INSTALL
=======

Clone this project somewhere your Python path can find it.

Add django-templates to INSTALLED_APPS

<pre>
INSTALLED_APPS = (
    ...
    'django-templates',
    ...
)
</pre>


USAGE
=====

To use django-templates, just extend the various base layouts. 

<pre>
{% extends 'html5boilerplate/base.html' %}

{% block header.content %}
    Helllllo World.
{% endblock header.content %}
</pre>
