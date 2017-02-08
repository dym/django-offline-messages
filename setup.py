# -*- coding: utf-8; mode: python; -*-
"""
A package that implements offline messages for Django
Web Framework.

(C) 2011-2014 oDesk www.oDesk.com w/revisions by Zapier.com
"""

from setuptools import setup

setup(
    name='django-offline-messages',
    version='0.3.7',
    description='A package that implements offline messages for Django plus more',
    long_description='A package that implements offline messages for Django Web Framework',
    license='BSD',
    keywords='django offline messages',
    url='https://github.com/dym/django-offline-messages',
    author='oDesk, www.odesk.com',
    author_email='developers@odesk.com',
    maintainer='Dmitriy Budashny',
    maintainer_email='dmitriy.budashny@gmail.com',
    packages=['offline_messages', 'offline_messages.migrations', 'offline_messages.south_migrations'],
    classifiers=['Development Status :: 3 - Alpha',
                 'Environment :: Web Environment',
                 'Framework :: Django',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: BSD License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Topic :: Software Development :: Libraries :: Python Modules',
                 ],
    test_suite='tests.runtests.runtests',
    install_requires=['django-jsonfield'],
    zip_safe=False
)
