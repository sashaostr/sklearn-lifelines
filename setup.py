#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools.command.test import test as TestCommand


from distutils.core import setup


exec(compile(open('sklearn_lifelines/__init__.py').read(),
                  'sklearn_lifelines/__init__.py', 'exec'))

setup(name='sklearn_lifelines',
      version=__version__,
      description='sklearn estimator wrappers for lifeline survival analysis Cox proportional hazard and Aalen Additive models from CamDavidsonPilon/lifelines',
      maintainer='sashaostr (Alexander Ostrikov)',
      maintainer_email='alexander.ostrikov@gmail.com',
      url='https://github.com/sashaostr/sklearn-lifeline.git',
      packages=['sklearn_lifelines'],
      keywords=['scikit', 'sklearn', 'pandas'],
      install_requires=[
          'lifelines >= 0.8.0.2',
          'scikit-learn>=0.13',
          'pandas>=0.11.0',
          'patsylearn'],
      # tests_require=['pytest', 'mock'],
      # cmdclass={'test': PyTest},
      )