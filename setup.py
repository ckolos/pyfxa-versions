#!/usr/bin/env python3

from setuptools import find_packages, setup


setup(
    author='ckolos',
    author_email='ckolos@mozilla.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Natural Language :: English',
        "Programming Language :: Python :: 3 :: Only",
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    entry_points={
        "console_scripts": [
            "pyfxa-versions = pyfxa_versions:main",
        ]
    },
    include_package_data=True,
    install_requires=[
        'requests<3.0.0',
        'click<8.0.0'
    ],
    license='MPLv2',
    name='pyfxa-versions',
    packages=find_packages(),
    package_data={
        "": ["*.txt"],
        "pyfxa_versions": ["data/pyfxa-versions.json"],
    },
    url='https://github.com/ckolos/pyfxa-versions',
    version='1.0.0',
)
