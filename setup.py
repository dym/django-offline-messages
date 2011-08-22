# -*- coding: utf-8; mode: python; -*-
"""
A package that implements offline messages for Django
Web Framework.
(C) 2011 oDesk www.oDesk.com
"""

from setuptools import setup

setup(
    name='django-offline-messages',
    version='0.2.5',
    description='A package that implements offline messages for Django',
    long_description='A package that implements offline messages for ' + \
                     'Django Web Framework',
    license='BSD',
    keywords='django offline messages',
    url='https://github.com/dym/django-offline-messages',
    author='oDesk, www.odesk.com',
    author_email='developers@odesk.com',
    maintainer='Dmitriy Budashny',
    maintainer_email='dmitriy.budashny@gmail.com',
    packages=['offline_messages',],
    classifiers=['Development Status :: 3 - Alpha',
                 'Environment :: Web Environment',
                 'Framework :: Django',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: BSD License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Topic :: Software Development :: Libraries :: Python Modules',
                 ],
    test_suite='tests.runtests.runtests'
    )
