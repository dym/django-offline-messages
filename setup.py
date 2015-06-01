# -*- coding: utf-8; mode: python; -*-
"""
A package that implements offline messages for Django
Web Framework.

(C) 2011 oDesk www.oDesk.com w/revisions by Zapier.com
"""

from setuptools import setup, find_packages

setup(
    name='fool-django-offline-messages',
    version='0.3.8.dev0',
    description='A package that implements offline messages for Django plus more',
    long_description='A package that implements offline messages for Django Web Framework',
    license='BSD',
    keywords='django offline messages',
    url='https://github.com/themotleyfool/django-offline-messages',
    author='Brian Faherty',
    author_email='bfaherty@fool.com',
    maintainer='Brian Faherty',
    maintainer_email='bfaherty@fool.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires = ['jsonfield', ],
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
