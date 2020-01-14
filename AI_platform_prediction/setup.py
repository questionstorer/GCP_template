from setuptools import setup
from setuptools import find_packages

REQUIRED_PACKAGES = [
    'tensorflow==1.14.0',
    'nltk==3.4.5'
]

setup(
    name='GCP_demo_prediction',
    version='0.1',
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(),
    include_package_data=True,
    scripts=['predictor.py']),
