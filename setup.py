# setup.py

from setuptools import setup, find_packages

setup(
    name="ec_project_manager",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "pyyaml",  # add others as needed
    ],
)
