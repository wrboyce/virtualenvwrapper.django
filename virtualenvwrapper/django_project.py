#!/usr/bin/env python
import logging
import os
import subprocess


logger = logging.getLogger(u'virtualenvwrapper.django')


def template(args):
    project_name = args.pop(0)
    project_template = os.path.join(os.path.dirname(__file__), 'templates', 'project_template')

    # Create a git-flow repository
    logger.info(u'Initialising git repo')
    subprocess.check_call(['git', 'init'])
    subprocess.check_call(['git', 'flow', 'init', '-d'])

    # Readline needs to be installed via `easy_install` or ipython gets upset
    logger.info(u'Installing readline')
    subprocess.check_call(['easy_install', 'readline'])

    # Install requirements via pip
    logger.info(u'Installing requirements')
    subprocess.check_call(['pip', 'install', '-r', os.path.join(project_template, 'requirements.txt')])

    # Create django project using our template
    logger.info(u'Creating django project')
    subprocess.check_call(['django-admin.py', 'startproject', '--template={}'.format(project_template), '-e', 'py', '-e', 'txt', project_name, os.getcwd()])

    # Commit changes to git, leaving a cleaning working environment
    logger.info(u'Committing changes')
    subprocess.check_call(['git', 'add', '.'])
    subprocess.check_call(['git', 'commit', '-m', '"[mkproject] installed Django project template"'])

    logger.info(u'Done')
