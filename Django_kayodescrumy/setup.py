import os
from setuptools import find_packages, setup
with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
	README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
	name='Django_kayodescrumy',
	version='0.1',
	packages=find_packages(),
	include_package_data=True,
	license='BSD License', # example license
	description='A simple Djando app.',
	long_description=README,
	url='',
	author='intelligentzombie',
	author_email='kayodeoshodi400@gmail.com',
	classifiers=[
		'Environment :: web Environment',
		'Framework :: Django',
		'Framework :: Django :: X.Y',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: BSD License', #example license
		'Operating System :: OS Independent',
		'Programing Language :: Python :: 3.8',
		'Topic :: Internet'

	],
)
