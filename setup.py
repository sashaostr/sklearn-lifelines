#!/usr/bin/env python

from setuptools import setup

setup(name='sklearn-lifeline',
      version='0.0.1',
      description='sklearn estimator wrappers for lifeline survival analysis Cox proportional hazard and Aalen Additive models from CamDavidsonPilon/lifelines',
      maintainer='sashaostr (Alexander Ostrikov)',
      maintainer_email='alexander.ostrikov@gmail.com',
      url='https://github.com/sashaostr/sklearn-lifeline.git',
      packages=['sklearn_lifelines'],
      keywords=['scikit', 'sklearn', 'pandas'],
      install_requires=[
          'lifelines >= 0.8.0.2'
          'scikit-learn>=0.13',
          'pandas>=0.11.0'],
      # tests_require=['pytest', 'mock'],
      # cmdclass={'test': PyTest},
      )