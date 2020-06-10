from setuptools import setup, find_packages

setup(
	name='my_package',
	version='1.0',
	url='https://github.com/MalikaL17/usefool_tips/my_package',
	author='Malika',
	author_email='some@email.com',
	description='This is my first test package',
	long_description=open('README.txt').read(),
	packages=find_packages(),
	install_requires=['numpy<=1.16.2']
)