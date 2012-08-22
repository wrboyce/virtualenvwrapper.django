#!/usr/bin/env python

from setuptools import setup, find_packages


setup(name='virtualenvwrapper.django',
      version='git',
      description='Awesome virtualenvwrapper Django project template',
      license="TBD",
      url='TBD',
      provides=('virtualenvwrapper.django',),
      requires=('virtualenv', 'virtualenvwrapper (>=2.9)'),
      packages=find_packages(),
      entry_points={'virtualenvwrapper.project.template': ('django = virtualenvwrapper.django_project:template',)})
