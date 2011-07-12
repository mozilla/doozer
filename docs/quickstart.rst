===========
Quick Start
===========

Here's the nitty-gritty, not-super-detailed "Getting Started" documentation for
Doozer.


Requirements
============

* Python 2.6

* `setuptools <http://pypi.python.org/pypi/setuptools#downloads>`_
  or `pip <http://pip.openplans.org/>`_.

* MySQL Server and client headers.

* Memcached Server.

* ``libjpeg`` and headers.

* ``zlib`` and headers.

* Several Python packages. See `Installing the Packages`_.

Since installation for these is very system-dependent, a package manager like
yum, aptitude, or brew is recommended.


Apache
------

To use Apache instead of the dev server, you'll need Apache with ``mod_wsgi``.


Get the Source
==============

Grab the source from Github::

    git clone --recursive git://github.com/mozilla/doozer.git
    cd doozer
    git clone --recursive git://github.com/mozilla/doozer-lib.git vendor


Installing the Packages
=======================

Compiled Packages
-----------------

There are a few packages that must or should be compiled. To install those, use
``pip``. (If you don't have ``pip``, you can get it with ``easy_install pip``.)

::

    sudo pip install -r requirements/compiled.txt


Python Packages
---------------

All the pure-Python requirements are stored in a git repository called the
"vendor library" or "vendor repo." If you followed the instructions in
**Get the Source** you should already have it cloned in the ``vendor/``
directory. (Note that the name of the vendor library must be cloned into the
``vendor/`` subdirectory of Doozer.)

To pick up updates to the vendor library, simply do::

    cd vendor
    git pull origin master
    git submodule update --init --recursive
    cd ..


Setup the Database
==================

Doozer requires a database and should use MySQL (other database engines, like
SQLite, may work but are not supported). You should create an empty database
and a user with all permissions::

    mysql> CREATE DATABASE doozer;
    mysql> GRANT ALL ON doozer.* TO doozer@localhost IDENTIFIED BY 'password';

Note the name of the database, the user, and the password for the next step.


Configuration
=============

Create a file named ``settings_local.py`` in the Doozer directory (i.e.
alongside ``manage.py`` and ``settings.py``). At the top, place this line::

    from settings import *

Now you can copy and modify settings from ``settings.py`` into
``settings_local.py`` and the value will override the default.


Database
--------

At a minimum, you need to define a database connection. Using the database
name, username, and password from above, you might use::

    DATABASES = {
        'default': {
            'NAME': 'doozer',
            'ENGINE': 'django.db.backends.mysql',
            'HOST': 'localhost',
            'USER': 'doozer',
            'PASSWORD': 'password',
            'OPTIONS': {'init_command': 'SET storage_engine=InnoDB'},
            'TEST_CHARSET': 'utf8',
            'TEST_COLLATION': 'utf8_unicode_ci',
        },
    }

You should be careful not to change the ``ENGINE``, ``OPTIONS``, or ``TEST_*``
settings.

Once the database connection settings are there, you can create the database
schema::

    ./vendor/src/schematic/schematic migrations/

This will run through the steps to create and update the database, though there
will be no data. You will likely need to create a superuser. This can be done
with Django's ``createsuperuser`` management command::

    ./manage.py createsuperuser

Just follow the prompts.


Uploads
=======

Doozer has the ability to upload images for screenshots. To make this work,
you'll need to create a directory (it's specifically *not* under version
control)::

    mkdir -p media/upload
    chmod -R a+w media/upload

Whoever the webserver is running as needs to be able to write to
``media/upload``.


Up and Running
==============

To see if you've got everything up and running, start the Django dev server::

    ./manage.py runserver

and navigate to ``http://localhost:8000/``. You should see the Doozer home
page!


Deploying with Apache
=====================

If you're deploying with Apache and ``mod_wsgi``, you'll need to know a couple
things:

* The WSGI endpoint is ``wsgi/doozer.wsgi``.
* The ``WSGIScriptAlias`` should be ``/``.
* You'll need to set up a couple ``Alias`` directives (below).

::

    Alias /media /path/to/doozer/media
    Alias /admin-media /path/to/doozer/vendor/django/django/contrib/admin/media
