# setup.py

from setuptools import setup, find_packages

setup(
    name="ec_project_manager",
    version="0.1.0",
    packages=find_packages(where="src") + find_packages(where="app"),
    package_dir={"": "src", "app": "app"},
    include_package_data=True,
    install_requires=[
        "loguru",
        "pyyaml", 
        "setuptools",
    ],
    # Add testing configuration
    test_suite='tests',
    tests_require=[
        'dotenv',
        'pytest',
        'pytest-cov',
    ],
    setup_requires=[
        'pytest-runner',
    ],
)
