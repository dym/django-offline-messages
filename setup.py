# -*- coding: utf-8; mode: python; -*-
"""
A package that implements offline messages for Django
Web Framework.
(C) 2011 oDesk www.oDesk.com
"""

from setuptools import setup, find_packages

setup(
    name='django-offline-messages',
    version='0.2.3',
    description='A package that implements offline messages for Django',
    long_description='A package that implements offline messages for' + \
                     'Django Web Framework',
    author='oDesk, www.odesk.com',
    author_email='developers@odesk.com',
    packages=['offline_messages',],
    classifiers=['Development Status :: 3 - Alpha',
                 'Environment :: Web Environment',
                 'Framework :: Django',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: BSD License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Topic :: Software Development :: Libraries :: Python Modules',
                 ]
    )
