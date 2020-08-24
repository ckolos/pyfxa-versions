#!/usr/bin/env python3

from setuptools import setup


setup(
    author='ckolos',
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
            "pyfxa-versions = ???:main",
        ]
    },
    include_package_data=True,
    install_requires=[
        'requests<3.0.0',
        'click<8.0.0'
    ],
    license='MPLv2',
    name='pyfxa-versions',
    packages=['pyfxa-versions'],
    package_data={
        "": ["*.txt"],
        "py-fxa-versions": ["data/py-fxa-versions.json"],
    },
    url='https://github.com/ckolos/py-fxa-versions',
    version='1.0.0',
)
