"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""
from setuptools import setup, find_packages
from codecs import open


def get_version():

    version_str = ''
    with open('version.txt') as ver_file:
        # logger.info("Getting version")
        version_str = ver_file.readline().rstrip()
        # logger.info("Got version {}".format(version_str))
    return version_str


def get_install_requires():
    with open('requirements.txt') as reqs_file:
        # logger.info("Finding For test_requirements")
        reqs = [line.rstrip() for line in reqs_file.readlines()]
        # logger.info("Found test_requirements {}".format(reqs))
    return {'test': reqs}


setup(name="Smart-Services",
      version=get_version(),
      packages=find_packages(exclude=['contrib', 'docs', 'tests*', 'coverage', 'bin', 'test*', 'evaluation', 'research', 'dependencies']),
      description='Test',
      install_requires=get_install_requires()
      )

