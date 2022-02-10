from setuptools import find_packages
from setuptools import setup

REQUIRED_PACKAGES = [
    'tensorflow==2.5.3',
    "tensorflow_datasets==1.3.2",
    'nltk==3.4.5'
]

setup(
    name='demo_imdb',
    version='0.1',
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(),
    include_package_data=True,
    description='demo for imdb on GCP'
)