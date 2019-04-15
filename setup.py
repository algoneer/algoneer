from distutils.core import setup
from setuptools import find_packages

setup(
    name='algoneer',
    python_requires='>=3',
    version='0.0.1',
    author='Andreas Dewes',
    author_email='andreas.dewes@7scientists.com',
    license='Affero GPL',
    url='https://github.com/algoneer/algoneer-py',
    packages=find_packages(),
    package_data={'': ['*.ini']},
    include_package_data=True,
    install_requires=['click'],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'algoneer = algoneer.cli.main:algoneer'
        ]
    },
    description='A Python binding for our algorithm test kit Algoneer.',
    long_description="""A Python binding for our algorithm test kit Algoneer.
"""
)
