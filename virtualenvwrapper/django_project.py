#!/usr/bin/env python
import logging
import os
import subprocess


logger = logging.getLogger(u'virtualenvwrapper.django')


def template(args):
    project_name = args.pop(0)
    project_template = os.path.join(os.path.dirname(__file__), 'project_template')

    logger.info(u'Installing readline')
    subprocess.check_call(['easy_install', 'readline'])
    logger.info(u'Installing requirements')
    subprocess.check_call(['pip', 'install', '-r', os.path.join(project_template, 'requirements.txt')])
    logger.info(u'Creating django project')
    subprocess.check_call(['django-admin.py', 'startproject', '--template={}'.format(project_template), '-e', 'py', '-e', 'txt', project_name, os.getcwd()])
    logger.info(u'Initialising git repo')
    subprocess.check_call(['git', 'init'])
    subprocess.check_call(['git', 'flow', 'init', '-d'])
    logger.info(u'Done')
