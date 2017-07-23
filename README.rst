===============================
django-xforwardedfor-middleware
===============================

Simple Django middleware to use the ``X-Forwarded-For`` header as the request IP.

Installation
------------

``pip install django-xforwardedfor-middleware==2.0``

django-xforwardedfor-middleware version 2.0 supports django 1.10 and newer.
You can install version 1.1 if you're still using older django.


Usage
-----

Just add ``x_forwarded_for.middleware.XForwardedForMiddleware`` to your middleware.

Warning
-------

This middleware is intended to get the user ip behind a trusted reverse proxy 
using the ``X-Forwarded-For`` header, which is set by the proxy.
If your app does not run behind such an proxy, the middleware is a security problem,
as clients can spoof the header.

For more information see the Django changelog:
https://docs.djangoproject.com/en/dev/releases/1.1/#removed-setremoteaddrfromforwardedfor-middleware
