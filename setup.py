#!/usr/bin/env python

from setuptools import setup


setup(name='virtualenvwrapper.django',
      version='git',
      description='Awesome virtualenvwrapper Django project template',
      author='Will Boyce',
      author_email='me@willboyce.com',
      url='http://github.com/wrboyce/virtualenvwrapper.django',
      provides=('virtualenvwrapper.django',),
      requires=('virtualenv', 'virtualenvwrapper (>=2.9)'),
      packages=['virtualenvwrapper'],
      package_data={'virtualenvwrapper': ['virtualenvwrapper/templates/app_template', 'virtualenvwrapper/templates/project_template']},
      entry_points={'virtualenvwrapper.project.template': ('django = virtualenvwrapper.django_project:template',)})
