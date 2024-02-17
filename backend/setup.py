# SPDX-FileCopyrightText: 2024 Tomás García Barreiro, Ángel Suárez Torres, Muhammad Imran
#
# SPDX-License-Identifier: MIT-0

from setuptools import find_packages, setup

setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'pandas'
    ],
)
