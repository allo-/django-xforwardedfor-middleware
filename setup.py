#!/usr/bin/env python
from setuptools import setup


setup(name='django-xforwardedfor-middleware',
      description='Django X-Forwarded-For Middleware',
      long_description='Use the X-Forwarded-For header to get the real ip of a request',
      author='Alexander Schier',
      author_email='allo@laxu.de',
      url='https://github.com/allo-/django-xforwardedfor-middleware',
      version='2.0',
      packages=['x_forwarded_for'],
      classifiers=[
          'Framework :: Django',
          'License :: Public Domain',
          'Operating System :: OS Independent',
          'Programming Language :: Python'
      ],
      install_requires=['django>=1.10']
      )

