from distutils.core import setup
from setuptools import find_packages

setup(
    name="algoneer",
    python_requires=">=3.6",
    version="0.0.2",
    author="Andreas Dewes",
    author_email="authors@algoneer.org",
    license="Mozilla Public License (MPL)",
    url="https://github.com/algoneer/algoneer",
    packages=find_packages(),
    package_data={"": ["*.ini"], "algoneer" : ['py.typed']},
    include_package_data=True,
    install_requires=["click", "pyyaml"],
    zip_safe=False,
    entry_points={"console_scripts": ["algoneer = algoneer.cli.main:algoneer"]},
    description="A Python toolkit for testing algorithmic systems and machine learning models.",
    long_description="""A Python toolkit for testing algorithmic systems and machine learning models.
""",
)
