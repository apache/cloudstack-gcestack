#!/usr/bin/env python
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import os

try:
    from setuptools import setup
except ImportError:
    try:
        from distribute_setup import use_setuptools
        use_setuptools()
        from setuptools import setup
    except ImportError:
        raise RuntimeError(
            "python setuptools is required to build gstack")

VERSION = '1.1.1'


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read().strip()

setup(
    name='gstack',
    version=VERSION,
    description='A GCE interface to Apache CloudStack',
    author='Ian Duffy, Darren Brogan, Sebastien Goasguen',
    author_email='ian@ianduffy.ie, brogand93@darrenbrogan.ie, runseb@gmail.com',
    long_description='A Google Compute Engine compliant interface to the Apache CloudStack API',
    url='https://github.com/NOPping/gstack',
    platforms=('Any'),
    license='LICENSE.txt',
    package_data={'': ['LICENSE.txt', 'data/*'],
                  'migrations': ['versions/*', '*.mako', '*.ini']},
    packages=[
        'gstack',
        'gstack.controllers',
        'gstack.models',
        'gstack.services',
        'gstack.data',
        'pyoauth2',
        'migrations'],
    include_package_data=True,
    install_requires=[
        'requests==2.20.0',
        'pycrypto==2.6',
        'pyopenssl',
        'Flask-SQLAlchemy',
        'flask',
        'alembic',
        'pyjwt'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
        'Programming Language :: Python :: 2.7',
    ],
    zip_safe=False,
    entry_points="""
        [console_scripts]
        gstack = gstack.__main__:main
        gstack-configure = gstack.configure:main
    """,
)
