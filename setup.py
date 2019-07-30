from distutils.core import setup
from setuptools import find_packages

setup(
    name="algoneer",
    python_requires=">=3",
    version="0.0.1",
    author="Andreas Dewes",
    author_email="andreas.dewes@algoneer.org",
    license="GNU Affero General Public License - Version 3 (AGPL-3)",
    url="https://github.com/algoneer/algoneer",
    packages=find_packages(),
    package_data={"": ["*.ini"]},
    include_package_data=True,
    install_requires=["click", "pyyaml"],
    zip_safe=False,
    entry_points={"console_scripts": ["algoneer = algoneer.cli.main:algoneer"]},
    description="A Python toolkit for testing algorithmic systems and machine learning models.",
    long_description="""A Python toolkit for testing algorithmic systems and machine learning models.
""",
)
