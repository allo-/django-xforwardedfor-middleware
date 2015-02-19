===============================
django-xforwardedfor-middleware
===============================

Simple Django middleware to use the `X-Forwarded-For` header as the request IP.

Installation
------------

  pip install django-xforwardedfor-middleware


Usage
-----

Just add `x_forwarded_for.middleware.XForwardedForMiddleware` to your middleware.
