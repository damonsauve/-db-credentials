from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

# Packaging:
# http://www.scotttorborg.com/python-packaging/
# sudo apt-get install python-setuptools
# python setup.py install
# python setup.py develop
# vi .gitignore -> http://www.scotttorborg.com/python-packaging/minimal.html
#
# Testing:
# sudo apt-get install python-pip
# pip install nose
# nosetests
#
setup(
    name='db_credentials',
    version='0.1',
    description="Reads databases credential files.",
    long_description=readme(),
    classifiers=['Programming Language :: Python :: 2.7'],
    url='',
    author='Damon Sauve',
    author_email='damonsauve@gmail.com',
    license='MIT',
    packages=['db_credentials'],
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
    tests_require=['nose'],
)
