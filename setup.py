#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

VERSION = '0.0.1'
LONG_DESC = """\
"""

setup(name='django-sitemerge',
      version=VERSION,
      description="",
      long_description=LONG_DESC,
      classifiers=[
          'Programming Language :: Python',
          'Operating System :: OS Independent',
          'Natural Language :: English',
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
      ],
      keywords='django',
      maintainer = 'Jason Kraus',
      maintainer_email = 'zbyte64@gmail.com',
      url='http://github.com/cuker/django-sitemerge',
      license='New BSD License',
      packages=find_packages(exclude=['test_environment']),
      #test_suite='setuptest.SetupTestSuite',
      #tests_require=(
      #  'django-setuptest',
      #  'django-dockit',
      #  #'-e git+git://github.com/zbyte64/django-dockit.git#egg=django-dockit',
      #),
      include_package_data = True,
      )
